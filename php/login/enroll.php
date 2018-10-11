<html>
	<body>
		<h1 align="center">
<?php
date_default_timezone_set("asia/hong_kong");
$currentTime=date("Y-m-d H:i:s");
print($currentTime);
//phpinfo();
?>
		</h1>
		
<?php
$connect=mysqli_connect("localhost","root","root");
//$createDB=mysqli_query($connect,"create database imau");
mysqli_select_db($connect,"imau");
?>
		<form>
			<table align="center">
				<tr>
					<td>CIN</td>
					<td><input type="text" name="cin"/></td>
				</tr>
				<tr>
					<td>NAME</td>
					<td><input type="text" name="name"  /></td>
				</tr>
				<tr>
					<td colspan="2"><input type="submit" name="submit" value="Submit" /></td>
				</tr>
			</table>
		</form>




<?php
$selectUsers="select * from users";
$result=mysqli_query($connect,$selectUsers);
?>
<table align="center" border="1">
<?php
while($row=mysqli_fetch_assoc($result)){
	print("<tr>");
		print("<th>");
			print("CIN");
		print("</th>");
		print("<th>");
			print("NAME");
		print("</th>");
	print("</tr>");
	print("<tr>");
		print("<td>");
				print($row["cin"]);
		print("</td>");
		print("<td>");
			print($row["name"]);		
		print("</td>");
	print("</tr>");
}
?>
</table>


	</body>
</html>