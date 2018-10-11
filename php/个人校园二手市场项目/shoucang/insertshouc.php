<?php
session_start();
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
	
if (isset($_GET["pid"]))
{
  $_SESSION["pid"] = $_GET["pid"];
}
$selectComments = "select user.userid,user.name,productname,description,picpath,postdate,teil,address,email from product inner join user on product.userid=user.userid and pid='".$_SESSION["pid"]."'";
$result = mysqli_query($connect, $selectComments);
while ($row = mysqli_fetch_assoc($result)){
	$inserts="insert into shoucang values('".$row['userid']."','".$_SESSION['pid']."','".$row['name']."','"
	.$row['teil']."','".$row['address']."','".$row['productname']."','".$row['email']."','".$row['description']."'
	,'".$row['picpath']."')";
   $resul = mysqli_query($connect, $inserts);	
	$p='xxxx='.$row['name'].'&&id='.$row['userid'];
	header("Location: ../productupload/blog.php?$p");
}
?>