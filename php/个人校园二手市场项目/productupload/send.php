<div class="col-md-3 categories-grid">
			<div class="search-in animated wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="500ms">
				<h4>发布商品</h4> 
				<div class="form-style-8">      
         	<form action="insertmessage.php?xxxx=<?php print $_GET['xxxx'].'&&id='.$_GET['id'];?>" enctype="multipart/form-data"  method="post">
<input type="text" name="productname" placeholder="商品名称" />
     <textarea placeholder="商品描述" onkeyup="adjust_textarea(this)" name="description"></textarea>
     <div class="file"> 选择图片    	
<input type="file" name="picpath"  placeholder="商品照片" /></div><br>
	<input type="submit" value="Submit" />
</form></div>
	</div>
