<div class="blog">
	<div class="container">
		<div class="menu-top">
				<div class="col-md-4 menu-left">
					<h3>最新影评</h3>
					<label><i class="glyphicon glyphicon-menu-up"></i></label>
					<span>欢迎一起分享的观影评论</span>
				</div>
				<div class="col-md-8 menu-right">
					<p> 电影评论的内容是多样的。有着重评论影片的题材、主题、人物或它的社会意义，也有专门论述不同片种、样式或影片的艺术风格、造型表现手段和电影语言的运用的；有对某一时期、某一流派的电影创作进行专题评论的，也有为著名的电影导演、演员等电影艺术家撰写评论的；既有在报刊上对当时上映的影片或某种创作问题写专栏评论的，也有对一定时期和范围内的影片进行评论的。由于读者和观众的欣赏境界或文化背景不同，所以既需要供电影专业工作者研究用的专题论文，也需要有提高一般观众欣赏水平的影评文章，这里有很多的看完电影的观后感，你可以把你的观影体验分享给大家。</p>
				</div>
				<div class="clearfix"></div>
			</div>
		<div class="col-md-9 blog-header">
			<div class=" blog-head">
			<?php
	$_number=1;		
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "db1");
$selectGallery = "select * from message";
$result = mysqli_query($connect, $selectGallery);
while ($row = mysqli_fetch_assoc($result))
{
  print'<div class="col-md-4 blog-top">';
  print'<div class="blog-in">';
  print "<a href='single.php?id=";print $row['id'];print"'>";
  print "<img class='img-responsive'";
  print "src='" . $row["picpath"] . "'";
  print ">";
  print "</img>";
  print "</a>";
  print "<div class='blog-grid'>"; 
  print "<h3><a href='single.php?id=";print $row['id'];print"'>";
  print $row["title"];
  print "</a></h3>";
  print "<div class='date'>";
  print "<span class='date-in'><i class="."'glyphicon glyphicon-calendar'></i>";
  print $row["postdate"];
  print "</span>";
  print "<a href='single.php?id=";print $row['id'];print "class="."'comments'><i class="."'glyphicon glyphicon-comment'></i>";
  print $row["name"];	
  print "</a>";
  print "<div class='clearfix'></div>";
  print "</div>";
  print "<p>";
  print $row["description"];
  print "</p>";
  print "</tr>";
 print "<div class='more'>";	
  print "<a class='link link-yaku' href='single.php?id=";print $row['id'];print "'><span>R</span><span>e</span><span>a</span>";
  print"<span>d</span> <span>M</span><span>o</span><span>r</span><span>e</span></a></div></div></div></div>";
  if($_number==3){print "<div class='clearfix'></div></div><div class='blog-head'>";$_number=0;}
  $_number++; 
}
?></div></div>

