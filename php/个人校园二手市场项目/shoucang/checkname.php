<?php 
if(isset($_GET["xxxx"])&&$_GET["xxxx"]!=null){
	$p='xxxx='.$_GET["xxxx"].'&&id='.$_GET["id"];
	header("Location: shouc.php?$p");}
	
else {header("Location: ../login/login.php");}


?>