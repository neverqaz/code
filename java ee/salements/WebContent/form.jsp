<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>hollow</title>
<script>
function writeCookie(){
	var d=new Date();
	d.setTime(d.getTime()+60*60*1000);
	document.Cookie="id=1001;expires="+d.toString();
}
</script>
</head>
<body>
<form action="read.jsp">
<table border=2 align="center" id="tablex">
<th align="center">选择产品</th>
<tr><td>产品编号</td><td>产品名称</td><td>产品价格</td><td>购买数量</td><td></td></tr>
<tr><td>1</td><td>iphone</td><td>1200</td><td><input type="text"size="2" id="s2"/></td><td><input type="button"value="加入购物车" onclick="writeCookie()"></td></tr>
<tr><td>2</td><td>iphonex</td><td>1600</td><td><input type="text" size="2" id="s3"/></td><td><input type="button"  value="加入购物车" onclick="writeCookie()" ></td></tr>
<tr><td>3</td><td>华为</td><td>1000</td><td><input type="text" size="2" id="s4"/></td><td><input type="button" value="加入购物车" onclick="writeCookie()"></td></tr>
<tr><td>4</td><td>oppo</td><td>800</td><td><input type="text" size="2" id="s5"/></td><td><input type="button"  value="加入购物车" onclick="writeCookie()"></td></tr>
</table>
<br><p align="center"><input type="submit" name="submit" value="submit"></p>
</form>
</body>
</html>