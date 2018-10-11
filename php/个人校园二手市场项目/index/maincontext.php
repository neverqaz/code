<div class="main_bg">
<div class="wrap">
<div class="main">
	<div class="top_main">
		<h2>最新发布的商品</h2>
		<a href="../productupload/checkname.php?xxxx=<?php if(isset($_GET["xxxx"])){print $_GET["xxxx"];print "&&id=".
				$_GET["id"];}else {$_GET["xxxx"]=null;print $_GET["xxxx"];}?>">查看更多</a>
		<div class="clear"></div>
	</div>
	<!-- start grids_of_3 -->
	<div class="grids_of_3">
		<?php $connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$selectGallery = "select * from product order by postdate desc";
$result = mysqli_query($connect, $selectGallery);
$_number=1;
while ($row = mysqli_fetch_assoc($result)){
       print"<div class='grid1_of_3'>";
			if (isset($_GET["xxxx"])&& $_GET["xxxx"]!=null){print"<a href='../detail/single.php?xxxx=".$row["name"]."&&pid=".$row['pid']."&&id=".$_GET['id']."'><img src='../productupload/".$row["picpath"]."'/><h3>".$row["productname"]."</h3><span class='price'>".$row["name"]."</span></a>";}
			else {print"<a href='../login/login.php'><img src='../productupload/".$row["picpath"]."'/><h3>".$row["productname"]."</h3><span class='price'>".$row["name"]."</span></a>";}
		print"</div>";
if($_number==3) {$_number=0;print"<div class='clear'></div></div><div class='grids_of_3'>";}
    $_number++;
	}?>
	<div class="clear"></div></div>

	<!-- start grids_of_2 -->
	
		</div>
		<div class="clear"></div>
	</div>
</div>
</div>
</div>
