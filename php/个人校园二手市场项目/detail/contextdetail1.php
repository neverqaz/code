<div class="main_bg">
<div class="wrap">
<div class="main">
  <!-- start content -->
  <div class="single">
      <!-- start span1_of_1 -->
      <div class="left_content">
      <div class="span1_of_1">
        <!-- start product_slider -->
        <div class="product-view">
            <div class="product-essential">
                <div class="product-img-box">
            <div class="more-views">
                <div class="more-views-container">
                <ul>
                    <li>
                      <a class="cs-fancybox-thumbs" data-fancybox-group="thumb"  href=""  title="" alt="">
                      <img src="" src_main=""  title="" alt="" /></a>            
                    </li>
                    <li>
                      <a class="cs-fancybox-thumbs" data-fancybox-group="thumb" href=""  title="" alt="">
                      <img src="" src_main=""  title="" alt="" /></a>
                    </li>
                    <li>
                      <a class="cs-fancybox-thumbs" data-fancybox-group="thumb"  href=""  title="" alt="">
                      <img src="" src_main=""  title="" alt="" /></a> 
                    </li>
                    <li>
                      <a class="cs-fancybox-thumbs" data-fancybox-group="thumb" href=""  title="" alt="">
                      <img src="" src_main="" title="" alt="" /></a>  
                    </li>
                    <li>
                      <a class="cs-fancybox-thumbs" data-fancybox-group="thumb"  href=""  title="" alt="">
                      <img src="" src_main="" title="" alt="" /></a>
                    </li>
                  </ul>
                </div>
            </div>
            <div class="product-image"> 
<?php
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
	
if (isset($_GET["pid"]))
{
  $_SESSION["pid"] = $_GET["pid"];
}
$selectComments = "select user.name,productname,description,picpath,postdate,teil,address,email from product inner join user on product.userid=user.userid and pid='".$_SESSION["pid"]."'";
$result = mysqli_query($connect, $selectComments);
?>
<?php
while ($row = mysqli_fetch_assoc($result)){

	print"<a class='cs-fancybox-thumbs cloud-zoom'";
	 print "rel=";
	 print"adjustX:30,adjustY:0,position:right,tint:#202020,tintOpacity:0.5,smoothMove:2,showTitle:true,titleOpacity:0.5"; 
     print "data-fancybox-group='thumb'";
     print "href='".$row["picpath"]."'>";
      print "<img src='../productupload/".$row["picpath"]."' />";
      print"</a></div>";

?>          
         
       
      <!-- end product_slider -->
      </div></div></div></div>
      <!-- start span1_of_1 -->

   <div class="span1_of_1_des">
          <div class="desc1">
     <?php 
  print "<h3>".$row["productname"]."</h3>";
  print" <h5>".$row["name"]."</h5>";
  print"<div class='available'><div class='btn_form'><form action='../shoucang/insertshouc.php?pid='";print $_SESSION["pid"]."'>
  <input type='submit' value='添加到收藏夹'/></form></div>";
  print"<span><a href='#'>".$row["teil"]."</a></span>";
  print"<span><a href='#'>".$row["email"]."</a></span>";
  print"<span><a href='#'>".$row["address"]."</a></span>";
  print"<p>".$row["description"]."</p>"; }
  
?>

        
          
          </div>
           </div>
          </div>
          <div class="clear"></div>