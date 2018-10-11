<html>
<body>
<?php 
date_default_timezone_set("asia/hong_kong");
$currentTime = date("Y-m-d H:i:s");
?>

<?php
if ($_FILES["picpath"])
{
	$pathname = "image/". $_FILES['picpath']['name'];
	move_uploaded_file($_FILES['picpath']['tmp_name'],$pathname);

}
session_start();
$password = $_SESSION["password"];
$name = $_SESSION["name"];
$id = $_SESSION["userid"];
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$insertCmts = "insert into followmicro values('".$id."',null,'".$_GET["mid"]."','".$name."',
'".$_POST["description"] ."','".$pathname."','".$currentTime."')";
$result = mysqli_query($connect, $insertCmts);
$p="xxxx=".$name."&&mid=".$_GET["mid"]."&&id=".$id;
print $p;
header("Location: microdetail.php?$p");
?>
</body>
</html>