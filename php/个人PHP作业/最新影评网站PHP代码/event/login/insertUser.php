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
$connect = mysqli_connect("localhost","root","123456");
mysqli_select_db($connect, "db1");
$insertUser = "insert into user values(null,'".
$_POST["name"]. 
"','" .
$_POST["password"]."')";
$result = mysqli_query($connect,$insertUser);
header("Location: ../index.html");
?>
</body>
</html>