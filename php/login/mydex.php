<html>
<body>
<h1 >
<?php
date_default_timezone_set("asia/hong_kong");
$currentTime =date("Y-m-d H:i:s");
Print($currentTime);
?>
</h1>

<?php
$connect=mysqli_connect("localhost","root","root");
mysqli_select_db($connect,"imau");
$selectuesrs=" select  *from users";
$result=mysqli_query($connect,$selectusers);?>
<table>
<tr>
<td>
cin
<\td> 
<td>
name
<\td>
<\tr>
<?php
while($row =mysqli_fetch_assoc($result)){
print("<tr>");
print("<td>");
print($row["cin"]);//����
print("<\td>");
print("<td>");
print($row["name"]);//����
print("<\td>");
print("<\tr>");
}
?>
</table>
</center>
</body>
</html>