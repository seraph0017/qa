#encoding:utf-8
from django.conf.urls import patterns, url
from bbs import views

urlpatterns = patterns('',

    url(r'^$',views.listing,name='index'),
    url(r'^(?P<topic_id>\d+)/$',views.details,name='detail'),
    url(r'^(?P<id>\d+)/commentshow/', views.details_show_comment, name='showcomment'),


    url(r'^publish/$',views.publish,name='publish'),
    url(r'^publish/v1/',views.publish_api,name='publish_api'),


)