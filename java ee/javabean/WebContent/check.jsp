<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<jsp:useBean id="newuser" class="javabean.User" scope="session">
<jsp:setProperty name="newuser" property="username"/>
<jsp:setProperty name="newuser" property="password"/>
<jsp:setProperty name="newuser" property="email"/>
<jsp:setProperty name="newuser" property="tel"/>
<jsp:setProperty name="newuser" property="address"/>
<jsp:setProperty name="newuser" property="gender"/>
</jsp:useBean>
<%
//校验信息
if(newuser.validate())response.sendRedirect("success.jsp");
else response.sendRedirect("failure.jsp");

%>
</body>
</html>