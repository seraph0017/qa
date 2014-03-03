#!/usr/bin/env python
#encoding:utf-8

from lettuce import *
from django.test.client import Client
from nose.tools import assert_equals
import lxml.html

@before.all
def set_browser():
    world.browser = Client()


@step(u"访问 <(.*)>")
def access_url(step,url):
    page = world.browser.get(url)
    world.html = lxml.html.fromstring(page.content)


@step(u"可以看到 <(.*)> 显示为 <(.*)>")
def see_header(step,target,content):
    title = world.html.cssselect(u'title')[0]
    assert_equals title.text == content