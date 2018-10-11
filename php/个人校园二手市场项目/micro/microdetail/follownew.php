<div class="col-md-3 categories-grid">
        <div class="blog-bottom animated wow fadeInUp animated" data-wow-duration="1000ms" data-wow-delay="500ms" style="visibility: visible; animation-duration: 1000ms; animation-delay: 500ms; animation-name: fadeInUp;">
            <h4>刚刚发布</h4>
              
                      <?php
      
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$selectGallery = "select * from micro order by postdate desc";
$result = mysqli_query($connect, $selectGallery);
?>

<?php 
while ($row = mysqli_fetch_assoc($result)){
print'<div class="product-go">';
  print "<a href='microdetail.php?xxxx=".$_SESSION["name"]."&&mid=".$row['mid']."&&id=".$_GET["id"]."' class='fashion'>";
  print "<img class='img-responsive1'";
  print "src='../".$row["picpath"]."'";
  print ">";
  print "</a>";
  print "<div class='grid-product'>"; 
  print "<a href='micro.php?xxxx=".$_SESSION["name"]."&&pid=".$row['mid']."&&id=".$_GET["id"]."' class='elit'>";
  print $row["title"];
  print "</a>";
  print "<p>";
  print $row["postdate"];
  print "</p></div><div class='clearfix'></div></div>";
}
?>
<div style="width: 100%;height: 30px; background-color:#98FB98; "></div>
  
          

        <div class="form-style-8">  

          <form action="insertfollowmicro.php?xxxx=<?php print $_GET['xxxx'].'&&mid='.$_GET['mid'];?>" enctype="multipart/form-data"  method="post">
<table>
  <tr ><td height="66.3667px" width="124px"><font size="+3" color="8E8E38" >留言</font><div class="bg"><img src="img/d.jpg"></div></td></tr><tr><td> <textarea placeholder="内容" onkeyup="adjust_textarea(this)" name="description" style="width: 255px;"></textarea></td></tr><tr><td><div class="file"> <div class="bg">    
            <img src="img/up.jpg" class="bg">    
       </div>       
<input type="file" name="picpath"  placeholder="商品照片" /></div> <div class="file"> <div class="bg">    
            <img src="img/ps.png" >    
       </div>       
<input type="submit" value="Submit" /></div></td></tr>
  
</table>
   </form></div>
<div style="width: 100%;height: 30px; background-color:#98FB98; "></div></div></div>
<div class="clearfix"> </div></div>
  
</div>              
                
                
                  
                
              