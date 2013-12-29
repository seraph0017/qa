#!/usr/bin/env python
#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 领域
class SpecialField(models.Model):

    field_title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.field_title

# 工具
class Tools(models.Model):

    tool_title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.tool_title

# 用户系统
class UserProfile(models.Model):

    user = models.ForeignKey(User,unique=True)
    screen_name = models.CharField('昵称',max_length=10,blank=False,null=False,help_text='长度1-10')
    fav_local = models.ForeignKey(SpecialField,related_name='user_specialfield')
    fav_tool = models.ForeignKey(Tools,related_name='user_tools')


    def __unicode__(self):
        return self.screen_name