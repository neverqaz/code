<!DOCTYPE html>
<html>
<head>
<title>Register</title>
<!-- for-mobile-apps -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
<link href="menu.css" rel="stylesheet" type="text/css" media="all" />
<!-- js -->
<script src="js/jquery.min.js"></script>
<!-- //js -->
<!-- cart -->
	<script src="js/simpleCart.min.js"> </script>
<!-- cart -->
<link rel="stylesheet" type="text/css" href="css/jquery-ui.css">
<!-- for bootstrap working -->
	<script type="text/javascript" src="js/bootstrap-3.1.1.min.js"></script>
<!-- //for bootstrap working -->
<link href='font/font.css' rel='stylesheet' type='text/css'>
<!-- animation-effect -->
<link href="css/animate.min.css" rel="stylesheet"> 
<script src="js/wow.min.js"></script>
</head>

<body>
<!-- header -->
<?php 
include("menu.php");?>
<div class="breadcrumbs">
		<div class="container">
			<ol class="breadcrumb breadcrumb1 animated wow slideInLeft" data-wow-delay=".5s">
				<li><a href="index.html"><span class="glyphicon glyphicon-home" aria-hidden="true"></span>首页</a></li>
				<li class="active">register</li>
			</ol>
		</div>
	</div>
<!-- //breadcrumbs -->
<!-- register -->
	<div class="register">
		<div class="container">
			<h3 class="animated wow zoomIn" data-wow-delay=".5s">Register Here</h3>
			<p class="est animated wow zoomIn" data-wow-delay=".5s">欢迎注册，感谢您加入我们的家庭</p>
			<div class="login-form-grids">
				<h5 class="animated wow slideInUp" data-wow-delay=".5s">个人信息</h5>
				<form class="animated wow slideInUp" data-wow-delay=".5s" action="insertUser.php" method="post">
					<input type="text" placeholder="姓名..."  name="name" >
					<input type="text" placeholder="电话号码..." name="teil" >
					<input type="text" placeholder="住在地址..." name="address" >
					<input type="radio" name="sex" value="1">男
                    <input type="radio" name="sex" value="2">女				
				<div class="register-check-box animated wow slideInUp" data-wow-delay=".5s">
					<div class="check">
						<label class="checkbox"><input type="checkbox" name="checkbox"><i></i>Subscribe to Newsletter</label>
					</div>
				</div>
				<h6 class="animated wow slideInUp" data-wow-delay=".5s">登录信息</h6>
					<input type="email" placeholder="请务必使用校园邮箱账号" name="email" >
					<input type="password" placeholder="密码" name="password">
					<input type="password" placeholder="校园卡卡号" name="compus_card" >
					<div class="register-check-box">
						<div class="check">
							<label class="checkbox"><input type="checkbox" name="accept" value="1"><i> </i>我接受以上所有条件</label>
						</div>
					</div>
					<input type="submit" value="Register">
				</form>
			</div>
			<div class="register-home animated wow slideInUp" data-wow-delay=".5s">
				
			</div>
		</div>
	</div>
<!-- //register -->
</body>
</html>
			
			
			
				
					
				
				
				
					
					
						
					
				
			
		