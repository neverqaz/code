<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>failure</title>
</head>
<body>
<jsp:useBean id="newuser" class="javabean.User" scope="session"/>
注册失败，原因如下:<br>
<%=newuser.getError("username") %><br>
<%=newuser.getError("password") %><br>
<%=newuser.getError("email") %><br>
</body>
</html>