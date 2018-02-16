# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import post
from django.shortcuts import render

# Create your views here.

def list_of_post(request):
    post1=post.objects.all()
    template={'blog/post/list_of_post.html'}
    context={'post': post1}
    return  render(request ,template,context)

