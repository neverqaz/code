<div class="blog">
	<div class="container">
		<div class="col-md-9 ">
		<!--content-->
<div class="single">
<?php
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
	
if (isset($_GET["mid"]))
{
  $_SESSION["mid"] = $_GET["mid"];
}
$selectComments = "select * from micro where mid='".$_SESSION["mid"]."'";
$result = mysqli_query($connect, $selectComments);
?>
<?php
while ($row = mysqli_fetch_assoc($result))
{
  print "<div class='single-top'>";
  print "<img class='img-responsive wow fadeInUp animated";print" data-wow-delay='";print".5s' "; 
  print "src='../".$row["picpath"]."'style='visibility: visible; animation-delay: 0.5s; animation-name: fadeInUp;'";
  print "/>";
  print "<div class='lone-line'><h4>";
  print $row["title"];
  print "</h4>";  
  print "<ul class='grid-blog'>";
  print"<li><span><i class='glyphicon glyphicon-time'></i>";
  print $row['postdate']."</span></li>";
  print "<li><a href='#'><i class='glyphicon glyphicon-comment'></i>".$row["name"]."</a></li>";
  print "<li><a href='#'><i class='glyphicon glyphicon-share'></i>Share</a></li></ul>";
  print "<p class='wow fadeInLeft animated' data-wow-delay="."'.5s'".">".$row["description"]."</p>";
  print"</div></div>";	
}?>
<div class='comment'><h3>评论区</h3>
<?php
$selectFollowComments = "select * from followmicro where mid=".$_SESSION['mid'];
$result = mysqli_query($connect, $selectFollowComments);
while ($row = mysqli_fetch_assoc($result))
{
  print "<div class='media wow fadeInLeft animated' data-wow-delay='.5s'style='visibility: visible; animation-delay: 0.5s; animation-name: fadeInLeft;'>";
  print "<div class='code-in'><p class='smith'><a href='#'>".$row['name']."</a><span>".$row['postdate']."
  </span></p><p class='reply'><a href='#'><i class='glyphicon glyphicon-repeat'></i>REPLY</a></p><div class='clearfix1'></div></div><div class='media-left'>";
  print "<a href='#'><img src=".$row['picpath']."></a></div><div class='media-body'><p>";
  print $row["description"];
  print "</p></div></div>";								
}
?>
	
		
		
</div>
<!---->
<!--//content-->

		</div><div class="leave">
    <?php include("send.php");?>
      </div></div><div style="width: 100%;height: 30px; background-color:#98FB98; "></div>