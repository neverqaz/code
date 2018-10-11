<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%int i=3;
session.setAttribute("var",i);
session.setAttribute("user", "aa");
%>
<c:set var="user" value="aaa" scope="session"></c:set>

<!--  <c:remove var="user" />-->
<form action="pol.jsp">姓名<input type="text"name="name"><br>
年龄<input type="text"name="age"><br>
爱好:阅读<input type="checkbox"name="hobby" value="read"><br>
游泳<input type="checkbox"name="hobby" value="swimming"><br>
<input type="submit" name="submit" value="submit">
</body>
</html>