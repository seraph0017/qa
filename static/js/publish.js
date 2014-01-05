// django send
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// get csrf
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getPublishArgs(arg) {
    var args = null;
        board = null;
        tag = null;

    args = document.referrer;
    if(args!=''&&args.indexOf('board')>0){
        args = args.split('?')[1];
        board = decodeURIComponent(args.split('&')[0].split('=')[1]);
        tag = decodeURIComponent(args.split('&')[1].split('=')[1]);
        if(arg=='board'){
            return board;
        }else if(arg=='tag'){
            return tag;
        }else{
            console.log('wrong')
        }
    }
}


$(document).ready(function(){
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    // 默认选中板块
    var selectboard = null;
    selectboard = getPublishArgs('board');
    $('#'+selectboard).attr("SELECTED","SELECTED");
    if(selectboard!=null){
        $('#J_board').hide();
    }

    $('#publishform').submit(function(){
        var data = null;
            title = $('#publishform input[name="title"]').val();
            content = $(document.getElementById('content_ifr').contentWindow.document.body).html();
            board = $('#publishform select[name="board"]').val();
            tags = $('#publishform select[name="field"]').val();
            nodes = $('input[name="tags"]');
            tags = "";

            csrftoken = getCookie('csrftoken');

            user = $('.J_user').text();
            baseurl = window.location.href;
            activeurl = [baseurl.split('/')[0],baseurl.split('/')[1],baseurl.split('/')[2]].join('/');
            status = null;
            for(var i=0;i<nodes.length;i++){
                if(nodes[i].checked){
                    tags+=(","+nodes.eq(i).val());
                }
            }

        // console.log('title',title,'content',content,'board',board,'email',user,'url',activeurl,'tags',tags);
        data = {
            'topic_title':title,
            'topic_content':content,
            'topic_board':board,
            'topic_tags':tags,
            'topic_author':user,
            'topic_status':'normal',
            'topic_is_top':'no',
            'topic_is_pub':'no',
        };
        $.post(activeurl+"/publish/v1/",data,function(json){
            // console.log(json);
            status = json['status'];
            if(status=='success'){
                // console.log(status);
                window.location.href=activeurl+'/'+json['id'];
            }
            
        });


        return false;

    });
})