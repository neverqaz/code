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
mysqli_select_db($connect, "db1");
$insertm = "insert into message values(null,'".$_POST["name"]."','".$_POST["title"]."','".
$_POST["description"]."','".$pathname."','".$currentTime."')";
$result = mysqli_query($connect, $insertm);
$insertm1 = "insert into message1 values(null,'".$_POST["name"]."','".$_POST["title"]."','".
$_POST["description"]."', '".$pathname."','".$currentTime."')";
$result1 = mysqli_query($connect, $insertm1);
header("Location: blog.php");
?>
</body>
</html>