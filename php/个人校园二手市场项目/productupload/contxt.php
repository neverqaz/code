<div class="blog">
	<div class="container">
		<div class="menu-top">
				<div class="col-md-4 menu-left">
					<h3>校园二手商品</h3>
					<label><i class="glyphicon glyphicon-menu-up"></i></label>
					<span>欢迎一起分享二手商品</span>
				</div>
				<div class="col-md-8 menu-right">
					<p> 二手交易成为了当代大学生课余生活的一大热门，伴随着学生的购买能力的提高和每年的升学和毕业，也存在着许多各种类型的二手商品。
          通过这个系统，卖方可以非常方便的发布自己的信息，浏览别人的发布的信息，还可以对各种二手商品信息横向比较，作出自己的最佳选择。</p>
				</div>
				<div class="clearfix"></div>
			</div>
		<div class="col-md-9 blog-header">
			<div class=" blog-head">
			<?php
	$_number=1;		
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$selectGallery = "select * from product inner join user on product.userid=user.userid";
$result = mysqli_query($connect, $selectGallery);
while ($row = mysqli_fetch_assoc($result))
{
  print'<div class="col-md-4 blog-top">';
  print'<div class="blog-in">';
  print "<a href='../detail/single.php?xxxx=".$row["name"]."&&pid=";print $row['pid'];print"&&id=".$_GET["id"]."'>";
  print "<img class='img-responsive'";
  print "src='" . $row["picpath"] . "'";
  print ">";
  print "</img>";
  print "</a>";
  print "<div class='blog-grid'>"; 
  print "<h3><a href='../detail/single.php?xxxx=".$row["name"]."&&pid=";print $row['pid'];print"&&id=".$_GET["id"]."'>";
  print $row["productname"];
  print "</a></h3>";
  print "<div class='date'>";
  print "<span class='date-in'><i class="."'glyphicon glyphicon-calendar'></i>";
  print $row["postdate"];
  print "</span>";
  print "<a href='../detail/single.php?xxxx=".$row["name"]."&&pid=";print $row['pid'];print "class="."'comments'><i class="."'glyphicon glyphicon-comment'></i>";
  print $row["name"]."<br>tel:".$row["teil"];	
  print "</a>";
  print "<div class='clearfix'></div>";
  print "</div>";
  print "<p>";
  print $row["description"];
  print "</p>";
  print "</tr>";
 print "<div class='more'>";	
  print "<a class='link link-yaku' href='../detail/single.php?xxxx=".$row["name"]."&&pid=";print $row['pid'];print"&&id=".$_GET["id"]."'><span>L</span><span>o</span><span>o</span>";
  print"<span>k</span> <span>M</span><span>o</span><span>r</span><span>e</span></a></div></div></div></div>";
  if($_number==3){print "<div class='clearfix'></div></div><div class='blog-head'>";$_number=0;}
  $_number++; 
}
?></div></div>

