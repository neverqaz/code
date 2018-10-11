<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>register</title>
</head>
<body>
<% if(session.getAttribute("newuser")!=null)
	session.removeAttribute("newuser");
	
	%>
<form action=check.jsp>
<table border=2 align="center">
<caption  ><h1 color="red">welcome to register everybody！</h1></caption>
<tr><td style="width: 18px; height: 15px;" align="center">username</td><td><input type="text" name="username" style="width: 150px; height: 15px;"></td></tr>
<tr><td style="width: 18px; height: 15px;"align="center">password</td><td ><input type="password" name="password" style="width: 150px; height: 15px;"></td></tr>
<tr><td style="width: 18px; height: 15px;"align="center">email</td><td><input type ="text" name ="email" style="width: 150px; height: 15px;"></td></tr>
<tr><td style="width: 18px; height: 15px;"align="center">tel</td><td ><input type ="text" name ="tel" style="width: 150px; height: 15px;"></td></tr>
<tr><td style="width: 18px; height: 15px;"align="center">address</td><td ><input type ="text" name ="address" style="width: 150px; height: 15px;"></td></tr>
<tr><td style="width: 18px; height: 15px;"align="center">gender</td><td align="center"><input type="radio" name="gender" value="meil">meil&nbsp;&nbsp;&nbsp;
<input type="radio" name="gender" value="fameil">fameil</td></tr>
<tr><td></td><td align="center"><input type="submit" name ="submit" value="submit">&nbsp;&nbsp;<input type="reset" name ="reset" value="reset"></td></tr>
</table>
</form>
</body>
</html>