from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls',namespace='account')),
    url(r'^', include('bbs.urls',namespace='bbs')),
    
)

urlpatterns += patterns((''),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/gs/blog/static'}
    ),
    (r'^comments/', include('django_comments.urls')),
    (r'^tinymce/', include('tinymce.urls')),
)