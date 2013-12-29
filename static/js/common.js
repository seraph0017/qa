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


    // active
    var cateactive = null,
        siteactive = null,
        baseurl = window.location.href;
        activeurl = [baseurl.split('/')[0],baseurl.split('/')[1],baseurl.split('/')[2]].join('/') 


    if(baseurl.indexOf('site')>=0){
        siteactive = baseurl.split('=')[1]
        $('#'+siteactive).addClass('active')
    }
    if(baseurl.split('/').length>4){
        cateactive = baseurl.split('/')[3]
        $('#'+cateactive).addClass('active')
    }


    // site filter
    $('#chinaluxus').click(function(){
        $('#siteswitch').val('chinaluxus');
    });
    $('#527motor').click(function(){
        $('#siteswitch').val('527motor');
    });
    $('#autohome').click(function(){
        $('#siteswitch').val('autohome');
    });
    $('#neeu').click(function(){
        $('#siteswitch').val('neeu');
    });

    // redirect
    $('.J_redi').click(function(){
        console.log('1111');
        window.location.href=activeurl+'/publish/';
    })


    // login and register
    $('form#loginform').submit(function() {
        var data = null;
            username = $('form#loginform input[name="username"]').val();
            password = $('form#loginform input[name="password"]').val();
            csrftoken = getCookie('csrftoken');
            status = null;

        data = {
            'username':username,
            'password':password
        };

        // console.log('username',username,'password',password,'csrftoken',csrftoken,activeurl+"login/")

        $.post(activeurl+"/account/login/",data,function(json){
            // returndata = eval("("+json+")"); 
            status = json['status']
            if(status=='already'){
                // console.log(json)
                $('ul.nav.navbar-nav.navbar-right').eq(0).replaceWith(
                        '<ul class="nav navbar-nav navbar-right"><li><a href="/account/logout/">'+json['username']+'</a></li></ul>'
                    )
                $('div#login button[data-dismiss="modal"]').eq(0).click();
            }else if(status=='not exist'){
                // console.log(json)
                $('form#loginform span').eq(0).replaceWith(
                        '<span class="label label-warning">邮箱或密码错误，请重新输入</span>'
                    )

            }else if(status=='type worong'){
                // console.log(json)
                $('form#loginform span').eq(0).replaceWith(
                        '<span class="label label-warning">邮箱或密码格式不正确，请重新输入</span>'
                    )
            }else{
                // console.log(json)
            }
            

        })
        // window.location.reload()
        
        return false;
    });

    $('form#regform').submit(function() {
        var data = null;
            username = $('form#regform input[name="username"]').val();
            screen_name = $('form#regform input[name="screen_name"]').val();
            password = $('form#regform input[name="password"]').val();
            csrftoken = getCookie('csrftoken');
            status = null;

        data = {
            'screen_name':screen_name,
            'username':username,
            'password':password
        };

        // console.log('username',username,'password',password,'csrftoken',csrftoken,activeurl+"login/")

        $.post(activeurl+"/account/regist/",data,function(json){
            // returndata = eval("("+json+")"); 
            status = json['status']
            if(status=='success'){
                console.log(json)
                $('div#reg button[data-dismiss="modal"]').eq(0).click();
                $('ul.navbar-right a[data-target="#login"]').eq(0).click();

            }else if(status=='already exist'){
                console.log(json)
                $('form#regform span').eq(0).replaceWith(
                        '<span class="label label-warning">该用户已存在，请重新输入用户名密码</span>'
                    )

            }else if(status=='type worong'){
                console.log(json)
                $('form#regform span').eq(0).replaceWith(
                        '<span class="label label-warning">昵称、邮箱或密码格式不正确，请重新输入</span>'
                    )
            }else{
                console.log(json)
            }
            

        })
        // window.location.reload()
        
        return false;
    });


   
});





// django send
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}



