<html>
<body>
<?php 
date_default_timezone_set("asia/hong_kong");
$currentTime = date("Y-m-d H:i:s");
?>

<?php
if ($_FILES["picpath"])
{
	$pathname = "images/". $_FILES['picpath']['name'];
	move_uploaded_file($_FILES['picpath']['tmp1_name'], $pathname);

}
session_start();
$password = $_SESSION["password"];
$name = $_SESSION["name"];
$id = $_SESSION["id"];
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "db1");
$insertCmts = "insert into followmessage values($id,null,'".$name."','".$_POST["title"]."',
'".$_POST["description"] ."','".$pathname."','".$currentTime."')";
$result = mysqli_query($connect, $insertCmts);
header("Location: single.php");
?>
</body>
</html>