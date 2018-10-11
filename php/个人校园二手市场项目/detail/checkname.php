<?php 
if(isset($_GET["xxxx"])&&$_GET["xxxx"]!=null){
	$p='xxxx='.$_GET["xxxx"].'&&pid='.$_GET["pid"];
	header("Location: single.php?$p");}
	
else {header("Location: ../login/login.php");}


?>