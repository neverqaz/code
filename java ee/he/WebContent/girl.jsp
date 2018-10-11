<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>girl</title>

</head>
<body bgcolor="pink"> <h1>welcom girl</h1>

<%@include file="count.jsp"%>
<% String s=(String)session.getAttribute("user"); 

if(s==null){
	out.print("你还没有登陆，请点击<a href='login.html'>这里登陆</a>");
	
}else{
	out.println("您好"+s);
	out.println("<h1>fail</h1>");
out.println("<a href='boy.jsp'>link2</a>");}
%>
</body>
</html>