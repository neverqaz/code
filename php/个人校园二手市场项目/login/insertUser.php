<html>
<body>
<h1 align="center">
<?php 
date_default_timezone_set("asia/hong_kong");
$currentTime = date("Y-m-d H:i:s");
print"insert user page";
?>
</h1>
<?php
$accept=1;
//if($_POST["accept"].values==1){$accept=1;}
if($_POST["sex"].values==1){$sex="男";}
else $sex="女";
$connect = mysqli_connect("localhost","root","123456");
mysqli_select_db($connect, "shop");
$insertUser = "insert into user values(null,'".$_POST["name"]."','".$_POST["teil"]."','".$_POST["address"]."','".$sex."','".$_POST["email"]."',
'".$_POST["password"]."','".$_POST["compus_card"]."','".$accept."')";
$result = mysqli_query($connect,$insertUser);
header("Location: login.php");
?>
</body>
</html>