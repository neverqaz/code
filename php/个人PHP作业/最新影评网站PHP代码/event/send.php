<div class="col-md-3 categories-grid">
			<div class="search-in animated wow fadeInUp" data-wow-duration="1000ms" data-wow-delay="500ms">
				<h4>发布影评</h4>       
         	<form action="insertmessage.php" enctype="multipart/form-data"  method="post">
      <table border="2">
<tr>
	<td>	
		Name
	</td>
	<td>
		<input type="text" name="name" value="
		<?php
			print $_SESSION['name'];
		?>
		" />
	</td>
</tr>
<tr>
<td>
标题
	</td>
	<td>
<input type="text" name="title" />
	</td>
</tr>
<tr>
	<td>
描述
	</td>
	<td>
		<textarea name="description">
			
		</textarea>
	</td>
	</tr>
	<tr>
	<td>
Pic
		</td>
		<td>
<input type="file" name="picpath" />
		</td>
	</tr>
	<tr>
	<td colspan="1">
	<input type="submit" value="Submit" />
	</td>
	</tr>
	</table>
</form>
	</div>
