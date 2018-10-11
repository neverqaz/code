<!DOCTYPE html>
<html>
<head>
<title>收藏夹</title>
<!-- for-mobile-apps -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="menu.css"/>
<link rel="stylesheet" type="text/css" href="footer.css"/>
	<link rel="stylesheet" type="text/css" href="context.css"/>
</head>
<?php include("menu.php")?>
<!-- checkout -->
	<div class="checkout">
		<div class="container">
			<h3 class="animated wow slideInLeft" data-wow-delay=".5s"> <span>收藏夹</span></h3>
			<div class="checkout-right animated wow slideInUp" data-wow-delay=".5s">
				<table class="timetable_sub">
					<thead>
						<tr><th>商品id</th>	
							<th>商品名</th>	
							<th>商品图片</th>
							<th>商品描述</th>
							<th>用户名</th>
							<th>邮箱</th>
							<th>地址</th>
							<th>删除</th>
						</tr>
					</thead>
					<?php
		$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");	
$selectComments = "select *from shoucang where userid=".$_GET["id"];
$result = mysqli_query($connect, $selectComments);
while ($row = mysqli_fetch_assoc($result)){
	$p='pid='.$row["pid"].'&&id='.$row["userid"];
print"<tr class='rem1'><td class='invert'>".$row["pid"]."</td><td class='invert'>"
	.$row["productname"]."</td><td class='invert-image'><a href='single.html'><img src='../productupload/"
	.$row["picpath"]."'class='img-responsive' /></a></td><td class='invert'>".$row["description"]."</td>
	<td class='invert'>".$row["name"]."</td><td class='invert'>".$row["email"]."</td><td class='invert'>"
	.$row["address"]."</td><td class='invert'><a href='deleteshouc.php?$p'>删除</a></td></tr>";}?>
				</table>
			</div>
			
		</div>
	</div>
<!-- //checkout -->
<!-- footer -->
<!-- //footer -->
<?php include("footer.php");?>
</body>
</html>