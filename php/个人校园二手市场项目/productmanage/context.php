	<div class="checkout">
		<div class="container">
			<h3 class="animated wow slideInLeft" data-wow-delay=".5s"><span>商品管理</span></h3>
			<div class="checkout-right animated wow slideInUp" data-wow-delay=".5s">
				<table class="timetable_sub">
					<thead>
						<tr><th>商品id</th>	
							<th>商品名称</th>	
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
$selectComments = "select * from product inner join user on product.userid=user.userid where user.userid=".$_GET["id"];
$result = mysqli_query($connect, $selectComments);
while ($row = mysqli_fetch_assoc($result)){
	$p='pid='.$row["pid"].'&&id='.$row["userid"]."&&xxxx=".$row["name"];
        $_SESSION["name"]=$row["name"];
print"<tr class='rem1'><td class='invert'>".$row["pid"]."</td><td class='invert'>"
	.$row["productname"]."</td><td class='invert-image'><a href='single.html'><img src='../productupload/"
	.$row["picpath"]."'class='img-responsive' /></a></td><td class='invert'>".$row["description"]."</td>
	<td class='invert'>".$row["name"]."</td><td class='invert'>".$row["email"]."</td><td class='invert'>"
	.$row["address"]."</td><td class='invert'><a href='deleteproduct.php?$p'>删除</a></td></tr>";}?>
				</table>
			</div>
			
		</div>
	</div>
		<div class="checkout">
		<div class="container">
			<h3 class="animated wow slideInLeft" data-wow-delay=".5s"><span>微话日记管理</span></h3>
			<div class="checkout-right animated wow slideInUp" data-wow-delay=".5s">
				<table class="timetable_sub">
					<thead>
						<tr><th>id</th>	
							<th>用户名</th>	
							<th>标题</th>
							<th>描述</th>
							<th>照片</th>
							<th>发布日期</th>
							<th>删除</th>
						</tr>
					</thead>
					<?php
		$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");	
$selectComments = "select * from micro where userid=".$_GET["id"];
$result = mysqli_query($connect, $selectComments);
while ($row = mysqli_fetch_assoc($result)){
	$p='mid='.$row["mid"].'&&id='.$row["userid"]."&&xxxx=".$row["name"];
print"<tr class='rem1'><td class='invert'>".$row["mid"]."</td><td class='invert'>"
	.$row["name"]."</td><td class='invert'>".$row["title"]."</td>
	<td class='invert'>".$row["description"]."</td><td class='invert-image'><a href='single.html'><img src='../micro/"
	.$row["picpath"]."'class='img-responsive' /></a></td><td class='invert'>"
	.$row["postdate"]."</td><td class='invert'><a href='deletemicro.php?$p'>删除</a></td></tr>";}?>
				</table>
			</div>
			
		</div>
	</div>