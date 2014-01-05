#encoding:utf-8
from django.db import models
from account.models import UserProfile, Tag
from django.forms import ModelForm


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
    topic_content = models.TextField()
    topic_time = models.DateTimeField(auto_now_add=True)

    topic_board = models.ForeignKey(Board,related_name='topic_board')
    topic_author = models.ForeignKey(UserProfile,related_name='topic_author')

    
    topic_tag = models.ManyToManyField(Tag)

    topic_final_comment_user = models.ForeignKey(UserProfile,related_name='topic_comment_user')
    topic_final_comment_time = models.DateTimeField()

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



















