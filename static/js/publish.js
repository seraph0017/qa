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

$(document).ready(function(){
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $('#publishform').submit(function(){
        var data = null;
            title = $('#publishform input[name="title"]').val();
            content = $('#publishform textarea[name="content"]').val();
            board = $('#publishform select[name="board"]').val();
            field = $('#publishform select[name="field"]').val();
            tool = $('#publishform select[name="tool"]').val();
            csrftoken = getCookie('csrftoken');
            user = $('.J_email').text();
            baseurl = window.location.href;
            activeurl = [baseurl.split('/')[0],baseurl.split('/')[1],baseurl.split('/')[2]].join('/');
            status = null;

        console.log('title',title,'content',content,'board',board,'field',field,'tool',tool,'email',user,'url',activeurl);
        data = {
            'topic_title':title,
            'topic_content':content,
            'topic_board':board,
            'topic_field':field,
            'topic_tool':tool,
            'topic_author':user,
            'topic_status':'normal',
            'topic_is_top':'no',
            'topic_is_pub':'no',
        };
        $.post(activeurl+"/publish/v1/",data,function(json){
            console.log(json);
            status = json['status'];
            if(status=='success'){
                // console.log(status);
                window.location.href=activeurl+'/'+json['id'];
            }
            
        });


        return false;

    });
})