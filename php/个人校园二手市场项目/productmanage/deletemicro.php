<?php
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$deleteUser="delete from micro where userid=".$_GET['id']." and mid=".$_GET['mid'];
$result= mysqli_query($connect, $deleteUser);
print $deleteUser;
$p="xxxx=".$_GET["xxxx"]."&&id=".$_GET["id"];
header("Location: main.php?$p");
?>
