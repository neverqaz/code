	<div class="left_sidebar">
		
				<h4>刚刚发布</h4>							
<?php			
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$selectGallery = "select * from product order by postdate desc";
$result = mysqli_query($connect, $selectGallery);
?>

<?php 
while ($row = mysqli_fetch_assoc($result)){
	print"<div class='left_products'><div class='left_img'>";
	print"<img src='../productupload/".$row["picpath"]."' /></div>";
print"<p><a href='#'>".$row["productname"]."</a></p><span>".$row["name"]."</span></div><div class='clear'></div>";
}
?>
			</div>
          	    <div class="clear"></div>
	       </div>	
	<!-- end content -->
	</div>
</div>
</div>