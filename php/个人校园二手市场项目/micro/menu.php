<div class="top_bg">
<div class="wrap">
	<div class="header">
		<div class="logo">
			<div class="logo-nav-left animated wow zoomIn" data-wow-delay=".5s">
				<ul><li><font color="white" size="+6">Second-Hand Market</font></li>
				</ul>	
				</div>
		</div>
		 <div class="log_reg">
				<ul>
					<?php 
					session_start();

					if (isset($_GET["xxxx"])&& $_GET["xxxx"]!=null){
						$_SESSION["name"]=$_GET["xxxx"];
						$_SESSION["userid"]=$_GET["id"];
						print "<a href='show.php'><li>".$_GET['xxxx']."</li><span class='log'> and </span><li>".$_SESSION["email"]."</li></a>";}
                      else {print"<li><a href='../login/login.php'>Login</a></li><span class='log'> or </span>
                      	<li><a href='../login/register.php'>Register</a></li>";}
                      ?>								   
					<div class="clear"></div>
				</ul>
		</div>	
		<div class="web_search">
		 	<form>
				<input type="text" value="" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = '';}">
				<input type="submit" value=" " />
			</form>
	    </div>						
		<div class="clear"></div>
	</div>	
</div>
</div>
<!-- start header_btm -->
<div class="wrap">
<div class="header_btm">
		<div class="menu_s">
			<ul>
				<li class="active"><a href="../index/show.php<?php if(isset($_GET["xxxx"]))print "?xxxx=".$_GET["xxxx"]."&&id=".$_GET["id"]; ?>">首页</a></li>
				<li><a href="../productupload/checkname.php?xxxx=<?php if(isset($_GET["xxxx"])){print $_GET["xxxx"];print "&&id=".
				$_GET["id"];}else {$_GET["xxxx"]=null;print $_GET["xxxx"];}?>">商品</a></li>
				<li><a href="../micro/checkname.php?xxxx=<?php if(isset($_GET["xxxx"])){print $_GET["xxxx"];print "&&id=".
				$_GET["id"];}else {$_GET["xxxx"]=null;print $_GET["xxxx"];}?>">微话题</a></li>
				<li><a href="../contact/contact.php?xxxx=<?php if(isset($_GET["xxxx"])){print $_GET["xxxx"];print "&&id=".$_GET["id"];}
				else {$_GET["xxxx"]=null; 
				print $_GET["xxxx"];}?>">联系我们</a></li>
				<div class="clear"></div>
			</ul>
		</div>
		
	<div class="header_right">
		<ul>
			<li><a href="../productmanage/checkname.php?xxxx=<?php if(isset($_GET["xxxx"])){print $_GET["xxxx"];print "&&id=".
				$_GET["id"];}else {$_GET["xxxx"]=null;print $_GET["xxxx"];}?>"><i  class="art"></i><span class="color1">个人管理</span></a></li>
			<li><a href="../shoucang/checkname.php?xxxx=<?php if(isset($_GET["xxxx"])){print $_GET["xxxx"];print "&&id=".
				$_GET["id"];}else {$_GET["xxxx"]=null;print $_GET["xxxx"];}?>"><i  class="cart"></i><span>收藏夹</span></a></li>
		</ul>
	</div>
	<div class="clear"></div>
</div>
</div>