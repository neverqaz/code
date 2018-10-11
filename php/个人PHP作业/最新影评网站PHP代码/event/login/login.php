<html>
<body>
<h1 align="center">
<?php 
date_default_timezone_set("asia/hong_kong");
$currentTime = date("Y-m-d H:i:s");
print($currentTime);
?>
</h1>

<?php
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect,"db1");
$queryUser = "select * from user where name='".$_POST["name"]."'and password ='".$_POST["password"] ."'";

$result = mysqli_query($connect, $queryUser);

if (mysqli_num_rows($result) == 0)
{
	header("Location: ..\index.html");
	exit;
}
if (mysqli_num_rows($result) > 0)
{
	session_start();
	$_SESSION['name']=$_POST["name"];
	$_SESSION['password']=$_POST["password"];
	header("Location: ..\blog.php");
}
	
#$row = mysqli_fetch_assoc($result);
#print $row["name"];
?>
</body>
</html>