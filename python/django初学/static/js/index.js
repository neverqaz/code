/**
 * Created by wybab on 2016/5/18.
 */
var data = {
    target: null,
    init: function () {
        var modal = $('#promote');
        var modalYes = $('#promote_btn');
        var greet = $('#greet');
        
        greet.click(function () {
            modal.modal();
        });
        
        modalYes.click(function (e) {
//            if ($('#question').val() == "" || $('#advice').val() == "" ) {
//                $('#alert').removeClass('alert-warning').addClass('alert-danger').html('问题反馈和课程反馈不能为空。');
//            } else
//            sendPost($('#question_info').serialize(),function (data) {
//                alert(data.desc);
        		orderSubmit(modal);
       // }
       //     );
        });
    }
};

$(function () {
    data.init();
});

function check(obj) {
	s = obj.value;
	var pattern = new RegExp(
			"[`~!#$^&*|{}''\\[\\]<>/~#￥……&*（）——|]");
	var rs = "";
	for (var i = 0; i < s.length; i++) {
		rs = rs + s.substr(i, 1).replace(pattern, '');
	}
	if (rs !== s) {
		alert("输入中不能包含非法字符!");
	}
	return;
}
function orderSubmit(modal) {
	// var name = question_info.name.value;
	var question = question_info.question.value;
	var advice = question_info.advice.value;
	if (question == "") {
		window.alert("问题反馈不能为空");
		question_info.question.focus();
		return;
	}
	if (advice == "") {
		window.alert("课程反馈不能为空");
		question_info.advice.focus();
		return;
	}
	question_info.submit();
    modal.modal('hide');
}

//function sendPost(data,success,async) {
//    if (typeof async == "undefined") async = true;
//    $.ajax({
//        url : "http://api.wangyu.website/send",
//        type : 'POST',
//        data : data,
//        dataType : 'json',
//        async : async,
//        //contentType : 'application/json',
//        success : function(data, status, xhr) {
////         Do Anything After get Return data    
//            success(data);
//        },
//        Error : function(xhr, error, exception) {
//            // handle the error.
//            alert(exception.toString());
//        }
//    });
//}