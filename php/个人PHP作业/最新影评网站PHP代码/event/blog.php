<!DOCTYPE html>
<html>
<head>
<title>Blog</title>
<link href="css/bootstrap.css" rel="stylesheet" type="text/css" media="all" />
<link href="css/style.css" rel="stylesheet" type="text/css" media="all" />	
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href='css/font.css' rel='stylesheet' type='text/css'>
<link href="css/styles.css" rel="stylesheet">
<link href="css/animate.min.css" rel="stylesheet"> 
</head>
<body><h1>
<?php session_start();print $_SESSION['name'];?></h1>
<?php include("menu.php");
 include("contxt.php");
 include("send.php");
 include("follownew.php");
 include("endx.php");
?>
</body>
</html>

