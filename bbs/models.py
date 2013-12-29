#encoding:utf-8
from django.db import models
from account.models import UserProfile, SpecialField, Tools
from django.forms import ModelForm
from tinymce.models import HTMLField
# 板块
class Board(models.Model):

    board_title = models.CharField(max_length=255)
    board_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.board_title




# 帖子
class Topic(models.Model):


    STATUS = (
        ('normal','正常'),
        ('locked','被锁定'),
    )

    IS_TOP = (
        ('yes','是'),
        ('no','否'),
    )

    IS_PUB = (
        ('yes','是'),
        ('no','否'),
    )

    topic_title = models.CharField(max_length=255)
    topic_content = HTMLField()
    topic_time = models.DateTimeField(auto_now_add=True)

    topic_board = models.ForeignKey(Board,related_name='topic_board')
    topic_author = models.ForeignKey(UserProfile,related_name='topic_author')

    topic_category = models.ForeignKey(SpecialField,related_name='topic_specialfield')

    topic_tool = models.ForeignKey(Tools,related_name='topic_tool')

    topic_status = models.CharField(
            max_length = 30,
            choices = STATUS,
            default = 'normal',
        )

    topic_is_top = models.CharField(
            max_length = 30,
            choices = IS_TOP,
            default = 'no',
        )

    topic_is_pub = models.CharField(
            max_length = 30,
            choices = IS_PUB,
            default = 'no',
        )

    def __unicode__(self):
        return self.topic_title







class BoardForm(ModelForm):
    class Meta:
        model = Board
        field = ['board_title']




class TopicForm(ModelForm):
    class Meta:
        model = Topic
        field = ['topic_title','topic_content','topic_board','topic_category','topic_tool']



















