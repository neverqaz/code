<html>
<body>
<h1 align="center">
<?php 
date_default_timezone_set("asia/hong_kong");
$currentTime = date("Y-m-d H:i:s");
?>
</h1>

<?php

if ($_FILES["picpath"])
{
	$pathname = "images/". $_FILES['picpath']['name'];
	move_uploaded_file($_FILES['picpath']['tmp_name'], $pathname);

}	
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$insertm = "insert into micro values('".$_GET["id"]."',null,'".$_GET["xxxx"]."','".$_POST["title"]."',
'".$_POST["description"]."','".$pathname."','".$currentTime."')";
$result = mysqli_query($connect, $insertm);
$p='xxxx='.$_GET["xxxx"].'&&id='.$_GET["id"];
header("Location: micro.php?$p");
?>
</body>
</html>