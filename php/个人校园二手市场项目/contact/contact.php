<!DOCTYPE html>
<html>
<head>
	<title>product manage</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="footer.css"/>
	<link rel="stylesheet" type="text/css" href="menu.css"/>
	<link rel="stylesheet" type="text/css" href="context.css"/>
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);
		function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- //for-mobile-apps -->
<link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />
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
<link href='font.css' rel='stylesheet' type='text/css'>

<!-- animation-effect -->
<link href="css/animate.min.css" rel="stylesheet"> 
<script src="js/wow.min.js"></script>
<script>
 new WOW().init();
</script>
</head>
<body>
<?php include("menu.php");
    ?>
<div class="container">
	<div style="
    padding-top: 4em;
    padding-right: 0px;
    padding-bottom: 2em;
    padding-left: 0px;
font-family: 'Open Sans Condensed', sans-serif;
font-size: 14px;
line-height: 1.42857143;
color: #333;">
			<h3><center>联系我们</center></h3>
			<p class="est">有问题及时反馈给我们，我们将尽快给您答复</p></div>
			<div class="mail-grids">
				<div class="col-md-8 mail-grid-left animated wow slideInLeft animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: slideInLeft;">
					<form>
						<input type="text" value="Name" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Name';}" required="">
						<input type="email" value="Email" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Email';}" required="">
						<input type="text" value="Subject" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Subject';}" required="">
						<textarea type="text" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Message...';}" required="" style="margin-left: 0px; margin-right: 0px; width: 732px;">Message...</textarea>
						<input type="submit" value="Submit Now">
					</form>
				</div>
				<div class="col-md-4 mail-grid-right animated wow slideInRight animated" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: slideInRight;">
					<div class="mail-grid-right1">
						<img src="1.jpg" alt=" " class="img-responsive">
						<h4>宋先生<span>工程小白</span></h4>
						<ul class="phone-mail">
							<li><i class="glyphicon glyphicon-earphone" aria-hidden="true"></i>Phone: 123456789</li>
							<li><i class="glyphicon glyphicon-envelope" aria-hidden="true"></i>Email: hello@peikasuosi.com</a></li>
						</ul>

					</div>
				</div>
				<div class="clearfix"> </div>
			</div>
		</div>
<?php include("footer.php");?>
</body>
</html>