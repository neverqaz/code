<?php
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$deleteUser="delete from shoucang where userid=".$_GET['id']." and pid=".$_GET['pid'];
$result= mysqli_query($connect, $deleteUser);
print $deleteUser;
$p="xxxx=".$_SESSION["name"]."&&id=".$_GET["id"];
header("Location: shouc.php?$p");
?>
