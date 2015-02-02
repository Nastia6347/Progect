# -*- coding: utf-8 -*-
__author__ = 'Nastia'
from django.forms import ModelForm
from models import *


class PostModel(ModelForm):
    class Meta:
        model = Post
        fields = ['fio', 'id_rating', 'content']