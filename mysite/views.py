# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from forms import *
from django.contrib import messages
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse

# Create your views here.


def company(request):
        return TemplateResponse(request, 'company.html')


def contacts(request):
        return TemplateResponse(request, 'contacts.html')


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/cabinet/', args)
        else:
            args['login_error'] = "Пользователь не найден"
            return TemplateResponse(request, 'login.html', args)
    else:
        return TemplateResponse(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/cabinet/', args)
        else:
            args['form'] = newuser_form
    return TemplateResponse(request, 'register.html', args)


def cabinet(request):
    args = {}
    args['username'] = request.user.username
    args['posts'] = Post.objects.filter(id_user=request.user.id)
    return TemplateResponse(request, 'cabinet.html', args)


def posts(request):
    all_posts = Post.objects.filter(is_active=True)
    if request.user.username:
        form = PostModel(initial={'fio': request.user.username})
    else:
        form = PostModel
    return TemplateResponse(request, 'posts.html', {'form': form, 'all_posts': all_posts})


def addpost(request):
    if request.POST:
        form = PostModel(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = datetime.datetime.now()
            if request.user.username:
                post.id_user = request.user
                if form.has_changed():
                    post.fio = post.fio
            form.save()
            messages.info(request, 'Thank you for your message.')
        return redirect('/posts/')