# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Progect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contacts/$', 'mysite.views.contacts'),
    url(r'^addpost/$', 'mysite.views.addpost'),
    url(r'^cabinet/$', 'mysite.views.cabinet'),
    url(r'^login/$', 'mysite.views.login'),
    url(r'^logout/$', 'mysite.views.logout'),
    url(r'^posts/$', 'mysite.views.posts'),
    url(r'^register/$', 'mysite.views.register'),
    url(r'^', 'mysite.views.company'),
)
