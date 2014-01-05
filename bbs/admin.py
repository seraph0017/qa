from django.contrib import admin
from models import *
# Register your models here.

class TopicAdmin(admin.ModelAdmin):

    class Media:
        js = ('js/tinymce/tiny_mce.js',
              'js/textareas.js')

admin.site.register(Board)
admin.site.register(Topic,TopicAdmin)

