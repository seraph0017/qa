#encoding:utf-8
import json
import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from models import Board,Topic, BoardForm, TopicForm
from account.models import UserProfile, Tag
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect



from django_comments.models import Comment
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required  
# Create your views here.


@csrf_protect
def listing(request):
    board = None
    tag = None
    query = None
    top_topic_list = []
    nor_topic_list = []

    # 公告贴
    pub_list = Topic.objects.filter(topic_is_pub='yes').order_by('-topic_final_comment_time')
    # 板块
    board_list = Board.objects.all()
    # 标签
    tags = Tag.objects.all()


    if 'board' in request.GET and request.GET['board'] != '':
        board = request.GET['board']
        board = Board.objects.get(board_title=board)

    if 'tag' in request.GET and request.GET['tag'] != '':
        tag = request.GET['tag']
        tag = Tag.objects.get(tag_name=tag)

    if 'query' in request.GET and request.GET['query'] != '':
        query = request.GET['query']


    # 如果有查询
    if query:
        topic_list = Topic.objects.filter(topic_is_pub='no',topic_title__contains=query).order_by('-topic_final_comment_time')
    elif board:
        if tag:
            topic_list = tag.topic_set.filter(topic_is_pub='no',topic_board=board).order_by('-topic_final_comment_time')
        else:
            topic_list = Topic.objects.filter(topic_is_pub='no',topic_board=board).order_by('-topic_final_comment_time')
    elif tag:
        topic_list = tag.topic_set.filter(topic_is_pub='no').order_by('-topic_final_comment_time')
    else:
        topic_list = Topic.objects.filter(topic_is_pub='no').order_by('-topic_final_comment_time')


    for topic in topic_list:
        if topic.topic_is_top == 'yes':
            top_topic_list.append(topic)
        else:
            nor_topic_list.append(topic)

    topic_list = top_topic_list + nor_topic_list



    

    return render_to_response('list.html',
            {
            "pub_list":pub_list,
            "topic_list":topic_list,

            "board_list":board_list,
            "board_info":board,

            "tags":tags,
            
            },
            context_instance = RequestContext(request)
    )



@csrf_protect
def details(request,topic_id):

    try:
        topic = Topic.objects.get(pk=topic_id)
        tags = topic.topic_tag.all()


    except Topic.DoesNotExist:
        raise Http404

    return render_to_response(
        'detail.html',
        {
        'topic':topic,

        'tags':tags,
        },
        context_instance = RequestContext(request),
    )
    

def details_show_comment(request, id=''):
    details = Topic.objects.get(id=id)
    

    return render_to_response(
        'details_comments_show.html', 
        {
        "details": details,

        }
        )




@login_required
@csrf_protect
def publish(request):


    boards = Board.objects.all().order_by('-board_time')
    
    tags = Tag.objects.all()
    
    return render_to_response(
            'publish.html',
            {
            'boards':boards,

            'tags':tags,
            },
            context_instance = RequestContext(request),
        )


@csrf_protect
def publish_api(request):

    if request.method == 'POST':
        data = request.POST

       

        new_board = Board.objects.get(board_title=data['topic_board'])


        new_user = User.objects.get(email=data['topic_author'])
        new_user_profile = UserProfile.objects.get(user=new_user)

        new_tags = data['topic_tags'].split(',')



        new_topic = Topic(
                topic_status = data['topic_status'],
                topic_is_top = data['topic_is_top'],
                topic_title = data['topic_title'],
                topic_content = data['topic_content'],
                topic_board = new_board,
                topic_author =new_user_profile,
               
                topic_is_pub = data['topic_is_pub'],
                topic_final_comment_time = datetime.datetime.now(),
                topic_final_comment_user = new_user_profile,
            )

        new_topic.save()

        for tag in new_tags:
            if tag != '':
                t = Tag.objects.get(tag_name=tag)
                new_topic.topic_tag.add(t)
                new_topic.save()

        

        return HttpResponse(json.dumps({
                    'status':'success',
                    'id':new_topic.id,
                },ensure_ascii=False),content_type="application/json")

    else:
        tf = TopicForm()

    return HttpResponse(json.dumps({
                    'status':'not post',
                },ensure_ascii=False),content_type="application/json")




@receiver(pre_save, sender=Comment)
def my_handler(sender, **kw):
    comment = kw['instance']
    topic = Topic.objects.get(pk=comment.object_pk)

    new_user = User.objects.get(email=comment.user_email)
    new_user_profile = UserProfile.objects.get(user=new_user)
    topic.topic_final_comment_user = new_user_profile
    topic.topic_final_comment_time = comment.submit_date


    topic.save()

























