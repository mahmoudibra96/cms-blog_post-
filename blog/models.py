# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class post(models.Model):
    STATUS_CHOICES=(
        ('draft' , 'Draft'),
        ('published' , 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=250)
    author =models.ForeignKey(User ,related_name='blog_posts')
    published = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')


    def __str__(self):
        return self.title