<div class="blog-bottom animated wow fadeInDown" data-wow-duration="1000ms" data-wow-delay="500ms">
						<h4>刚刚发布</h4>
							
											<?php
			
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "db1");
$selectGallery = "select * from message order by postdate desc";
$result = mysqli_query($connect, $selectGallery);
?>

<?php 
while ($row = mysqli_fetch_assoc($result)){
print'<div class="product-go">';
  print "<a href='single.php?id=".$row['id']."' class='fashion'>";
  print "<img class='img-responsive'";
  print "src='" . $row["picpath"] . "'";
  print ">";
  print "</img>";
  print "</a>";
  print "<div class='grid-product'>"; 
  print "<a href='single.php?id=".$row['id']."' class='elit'>";
  print $row["title"];
  print "</a>";
  print "<p>";
  print $row["description"];
  print "</p></div><div class='clearfix'></div></div>";
}
?>
</div>
<div class="clearfix"> </div>
	</div>
</div>							
								
									
									
								
							