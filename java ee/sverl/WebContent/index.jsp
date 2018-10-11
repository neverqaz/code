<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="login">
<input type="text" name="p">
<input type="submit" value="submit">
</form><br>
<a href="test.jsp?param=abc">link</a>
<br>当前在线用户：<%=application.getAttribute("count") %>
<br>当前登陆用户：<%=session.getAttribute("logcount") %>
<br>
<a href="logout.jsp">退出登录</a>
</body>
</html>