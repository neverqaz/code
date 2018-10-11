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
mysqli_select_db($connect,"shop");
$queryUser = "select * from user where email='".$_POST["email"]."'and password ='".$_POST["password"] ."'";
$result = mysqli_query($connect, $queryUser);

if (mysqli_num_rows($result) == 0)
{
	header("Location: login.php");
	exit;
}
if (mysqli_num_rows($result) > 0)
{   session_start();
	$row=mysqli_fetch_assoc($result);
	//$p='username='.$row['name'].'&userid='.$row['userid'].'&email='.$_POST["email"];
	//$_SESSION['name']=$row["name"];
	//$_SESSION['userid']=$row["userid"];
	$_SESSION['email']=$_POST["email"];
	$_SESSION['password']=$_POST["password"];
	$p='xxxx='.$row['name'].'&&id='.$row["userid"];
	header("Location: ..\index\show.php?$p");
}
	
#$row = mysqli_fetch_assoc($result);
#print $row["name"];
?>
</body>
</html>