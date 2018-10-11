<html>
	<body>
		<h1 align="center">
<?php
date_default_timezone_set("asia/hong_kong");
$currentTime=date("Y-m-d H:i:s");
print($currentTime);
//phpinfo();
?>
		</h1>
		
<?php
$connect=mysqli_connect("localhost","root","root");
mysqli_select_db($connect,"imau");
$insertUsers="insert into users  values('".$_POST["cin"].
										"','".$_POST["name"].
										"')";
$result=mysqli_query($connect,$insertUsers);
?>


	</body>
</html>