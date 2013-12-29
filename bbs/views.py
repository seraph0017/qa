#encoding:utf-8
import json
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from models import Board,Topic, BoardForm, TopicForm
from account.models import UserProfile, SpecialField, Tools
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from account.models import SpecialField, Tools

# Create your views here.


@csrf_protect
def listing(request):

    pub_list = Topic.objects.all().order_by('-topic_time')




    return render_to_response('list.html',
            {
            "pub_list":pub_list,
            },
            context_instance = RequestContext(request)
    )



@csrf_protect
def details(request,topic_id):

    try:
        topic = Topic.objects.get(pk=topic_id)
        topic_recent = Topic.objects.all().order_by('-topic_time')[:10]

    except Topic.DoesNotExist:
        raise Http404

    return render_to_response(
        'detail.html',
        {
        'topic':topic,
        'topic_recent':topic_recent,
        },
        context_instance = RequestContext(request),
    )
    

def details_show_comment(request, id=''):
    details = Topic.objects.get(id=id)
    return render_to_response('details_comments_show.html', {"details": details})





@csrf_protect
def publish(request):


    boards = Board.objects.all().order_by('-board_time')
    spfields = SpecialField.objects.all()
    tools = Tools.objects.all()
    
    return render_to_response(
            'publish.html',
            {
            'boards':boards,
            'spfields':spfields,
            'tools':tools,
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

        new_field = SpecialField.objects.get(field_title=data['topic_field'])
        new_tool = Tools.objects.get(tool_title=data['topic_tool'])

        new_topic = Topic(
                topic_status = data['topic_status'],
                topic_is_top = data['topic_is_top'],
                topic_title = data['topic_title'],
                topic_content = data['topic_content'],
                topic_board = new_board,
                topic_author =new_user_profile,
                topic_category = new_field,
                topic_tool = new_tool,
                topic_is_pub = data['topic_is_pub'],
            )

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




        





















