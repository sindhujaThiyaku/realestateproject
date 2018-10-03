$("#loginhref").click(function(){
	$("#registerPage").show();
	$("#loginPage").hide();
})

$("#registerhref").click(function(){
	$("#loginPage").show();
	$("#registerPage").hide();
})

$("#btn-reset").click(function(){
	$('#username').val("");
	$('#usermail').val("");
	$('#userpswd').val("");
	$('#usercpswd').val("");
	$('#usernumber').val("");
	$('#p0').text("");
	$('#p1').text("");
	$('#p2').text("");
	$('#p3').text("");
	$('#p4').text("");

})

function ajaxCall(type,url,data,async){
	var status = false;
	$.ajax({
		type:type,
		url:url,
		data:data,
		async:async,
	}).done(function(json_data){
			status = json_data;
	});
	return status;
}

$("#btn-signup").click(function(){
	var username = $('#username').val();
	var usermail = $('#usermail').val();
	var userpswd = $('#userpswd').val();
	var usercpswd = $('#usercpswd').val();
	var usernumber = $('#usernumber').val();

	var name_regex = /^[0-9a-zA-Z]+$/;
	var email_regex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,4}$/;
	var password_regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/;
	var mobile_regex = /^([0|\+[0-9]{1,5})?([7-9][0-9]{9})$/;

	if (username.length == 0) {
		$('#p0').text("* All fields are mandatory *").css({ 'color': 'white', 'font-size': '100%' }); 
		$("#username").focus();
		return false;
	}
	else if(!username.match(name_regex)) {
	$('#p1').text("* Please enter valid user name with alphabets and numbers combination *").css({ 'color': 'white', 'font-size': '100%' });
	$("#username").focus();
	return false;
	}
	else if (!usermail.match(email_regex) || usermail.length == 0) {
	$('#p2').text("* Please enter valid email address *").css({ 'color': 'white', 'font-size': '100%' }); 
	$("#usermail").focus();
	return false;
	}
	else if (!userpswd.match(password_regex) || userpswd.length == 0) {
	$('#p3').text("* Please enter a valid password *").css({ 'color': 'white', 'font-size': '100%' }); 
	$("#userpswd").focus();
	return false;
	}
	else if ((usercpswd!=userpswd)||usercpswd.length==0) {
	$('#p4').text("* Please enter the correct password as entered above*").css({ 'color': 'white', 'font-size': '100%' }); 
	$("#usercpswd").focus();
	return false;
	}
	else if (!usernumber.match(mobile_regex) || usernumber.length == 0) {
	$('#p5').text("* Please enter the valid mobile number *").css({ 'color': 'white', 'font-size': '100%' }); 
	$("#usernumber").focus();
	return false;
	}
	else {
		ajaxCall('POST','user_register/',{"username":username,"email":usermail,"password":userpswd,"mobile_number":usernumber,'is_active':false,csrfmiddlewaretoken:getCookie('csrftoken')},true)
	}


})


$("#btn-signin").click(function(){
	var loginusername = $('#loginuser').val();
	var loginuserpswd = $('#loginpwd').val();
	if(loginusername==''){
		$('#p6').text("* Please enter the username").css({ 'color': 'white', 'font-size': '100%' }); 
		$("#loginuser").focus();
		return false;
	}
	else if(loginuserpswd==''){
		$('#p7').text("* Please enter the Password").css({ 'color': 'white', 'font-size': '100%' }); 
		$("#loginpwd").focus();
		return false;
	}
	else if(loginusername==''&& loginuserpswd==''){
		$('#p6').text("* Please enter the username").css({ 'color': 'white', 'font-size': '100%' }); 
		$("#loginuser").focus();
		$('#p7').text("* Please enter the Password").css({ 'color': 'white', 'font-size': '100%' }); 
		$("#loginpwd").focus();
		return false;
	}
	else{
		returnStatus = ajaxCall('POST','/login/user_login/',{'username':loginusername,'userpswd':loginuserpswd,csrfmiddlewaretoken:getCookie('csrftoken')},false)
		localStorage.setItem('token', JSON.stringify(returnStatus['token']));
		if(returnStatus['status']==1 && returnStatus['token']!=undefined){
		window.location.href = "/home/"
	}
	else{
		window.location.href = "/login/"
	}
	}
	
})
$("#loginuser,#loginpwd").keypress(function(){
		$('#p6').text("")
		$('#p7').text("")
})

