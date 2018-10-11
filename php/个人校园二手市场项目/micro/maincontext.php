<div class="content-top-top">
	<div class="container1">
		<div class="content-top">
					

				<div class="form-style-8">  

         	<form action="insertmicro.php?xxxx=<?php print $_GET['xxxx'].'&&id='.$_GET['id'];?>" enctype="multipart/form-data"  method="post">
<table>
	<tr ><td colspan="" rowspan="" headers=""><font size="+3" color="8E8E38" >微话日记</font><div class="bg"><img src="img/d.jpg"></div></td><td ><input type="text" name="tltle" placeholder="标题" /></td><td> <textarea placeholder="描述" onkeyup="adjust_textarea(this)" name="description"></textarea></td><td><div class="file"> <div class="bg">    
            <img src="img/up.jpg" >    
       </div>     	
<input type="file" name="picpath"  placeholder="商品照片" /></div></td><td> <div class="file"> <div class="bg">    
            <img src="img/ps.png" >    
       </div>     	
<input type="submit" value="Submit" /></div></td></tr>
	
</table>
   </form></div></div></div>
		<div class="container">
			<div class="content-top">
				<div class="col-md-4 content-left animated wow fadeInLeft animated" data-wow-duration="1000ms" data-wow-delay="500ms" style="visibility: visible; animation-duration: 1000ms; animation-delay: 500ms; animation-name: fadeInLeft;">
					<h3>微话题</h3>
					<label><i class="glyphicon glyphicon-menu-up"></i></label><br>
					<span>可以聊天，互动，交友</span>
				</div>
				<div class="col-md-8 content-right animated wow fadeInRight animated" data-wow-duration="1000ms" data-wow-delay="500ms" style="visibility: visible; animation-duration: 1000ms; animation-delay: 500ms; animation-name: fadeInRight;">
					<p>学生交友是为了在大学的生活中过的更加充实，通过该平台可以结识来自全国各地的农大学生。而该平台也正是基于网络平台的广泛性、互通性、娱乐性、经济性、安全性等优点的一种网络交流方式中的互动型服务微平台。专门为本校学生服务，类似农大表白墙的功能，大家可以在这里畅所欲言。可以发一些平时的动态。</p>
				</div>
				<div class="clearfix"> </div>
			</div>
			<div class="news-bottom">
				<div class="news-bot">
<?php
	$_number=1;		
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "shop");
$selectGallery = "select * from micro  order by postdate desc";
$result = mysqli_query($connect, $selectGallery);
while ($row = mysqli_fetch_assoc($result))
{$_SESSION["sendpname"]=$row["name"];
					print"<div class='col-md-6 news-bottom1 animated wow fadeInUp animated' data-wow-duration='1000ms' data-wow-delay='500ms'style='visibility: visible; animation-duration: 1000ms; animation-delay: 500ms; animation-name: fadeInUp;'>
						<a  href='microdetail/microdetail.php?xxxx=".$_GET['xxxx']."&&mid=".$row['mid']."&&id=".$_GET['id']."'class='a1'>
							<div class='content-item' style='background: url(".$row["picpath"].") no-repeat;background-size:cover;'>
							<div class='overlay'></div><div class=' news-bottom2'><ul class='grid-news'><li><span><i 
							class='glyphicon glyphicon-calendar'> </i>".$row["postdate"]."</span><b>/</b></li><li><span><i 
							class='glyphicon glyphicon-comment'> </i>".$row["name"]."</span><b>/</b></li><li><span><i 
							class='glyphicon glyphicon-share'> </i>".$row["title"]."</span></li></ul><p>".$row["description"]."</p></div></div>
                       </a></div>";
					if($_number==2){print"<div class='clearfix'> </div></div><div class='news-bot'>";$_number=0;}
			$_number++;}?>

				
			
			</div>
		</div>
	</div>
