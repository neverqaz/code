<div class="blog">
	<div class="container">
		
		<div class="col-md-9 ">
		<!--content-->
<div class="single">
<?php
$connect = mysqli_connect("localhost","root", "123456");
mysqli_select_db($connect, "db1");
	session_start();
if (isset($_GET["id"]))
{
  $_SESSION["id"] = $_GET["id"];
}
$selectComments = "select * from message where id='".$_SESSION["id"]."'";
$result = mysqli_query($connect, $selectComments);
?>
<?php
while ($row = mysqli_fetch_assoc($result))
{
  print "<div class='single-top'>";
  print "<img class='img-responsive wow fadeInUp animated";print" data-wow-delay='";print".5s' "; 
  print "src='".$row["picpath"]."'";
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
<div class='comment'><h3>Comments</h3>
<?php
$selectFollowComments = "select * from followmessage where id=".$_SESSION['id'];
$result = mysqli_query($connect, $selectFollowComments);
while ($row = mysqli_fetch_assoc($result))
{
  print "<div class='media wow fadeInLeft animated' data-wow-delay='.5s'>";
  print "<div class='code-in'><p class='smith'><a href='#'>".$row['name']."</a><span>".$row['postdate']."
  </span></p><p class='reply'><a href='#'><i class='glyphicon glyphicon-repeat'></i>REPLY</a></p><div class='clearfix'></div></div><div class='media-left'>";
  print "<a href='#'><img src=".$row['picpath']."></a></div><div class='media-body'><p>";
  print $row["description"];
  print "</p></div></div>";								
}
?>
</div>		
		<div class="leave">
			<h3>Leave a comment</h3>
				<form action="insertfollowmessage.php" method="post" enctype="multipart/form-data">
					<div class="single-grid wow fadeInLeft animated" data-wow-delay=".5s">
							<input type="text" value="title" name="title"onfocus="this.value='';" onblur="if (this.value == '') {this.value = 'title';}">
							<textarea value="comment" name="description"onfocus="this.value='';" onblur="if (this.value == '') {this.value = 'Comment';}">Comment</textarea>
							<input type="file" name="picpath" />
						<label class="hvr-rectangle-out">
								<input type="submit" value="Send">
						</label>						
				</div>
				</form>
			</div>
		
</div>
<!---->
<!--//content-->

		</div>