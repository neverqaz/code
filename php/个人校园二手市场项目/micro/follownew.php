 <div class="col-md-6 news-bottom1 animated wow fadeInDown animated" data-wow-duration="1000ms" data-wow-delay="500ms" style="visibility: visible; animation-duration: 1000ms; animation-delay: 500ms; animation-name: fadeInDown;">
						<h4>刚刚发布</h4>
							
											<?php
			
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$selectGallery = "select * from product order by postdate desc";
$result = mysqli_query($connect, $selectGallery);
?>

<?php 
while ($row = mysqli_fetch_assoc($result)){
print'<div class="product-go">';
  print "<a href='../detail/single.php?xxxx=".$row["name"]."&&pid=".$row['pid']."' class='fashion'>";
  print "<img class='img-responsive1'";
  print "src='" . $row["picpath"] . "'";
  print ">";
  print "</img>";
  print "</a>";
  print "<div class='grid-product'>"; 
  print "<a href='../detail/single.php?xxxx=".$row["name"]."&&pid=".$row['pid']."' class='elit'>";
  print $row["productname"];
  print "</a>";
  print "<p>";
  print $row["description"];
  print "</p></div><div class='clearfix'></div></div>";
}
?>
</div>
<div class="clearfix"> </div>
	</div>
						
								
									
									
								
							