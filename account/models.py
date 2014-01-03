#!/usr/bin/env python
#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# tags
class Tag(models.Model):

    tag_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tag_name

# 用户系统
class UserProfile(models.Model):

    user = models.ForeignKey(User,unique=True)
    screen_name = models.CharField('昵称',max_length=10,blank=False,null=False,help_text='长度1-10')
    


    def __unicode__(self):
        return self.screen_name