<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>success</title>
</head>
<body>
注册信息如下：
<br>
<jsp:useBean id="newuser" class="javabean.User" scope="session"/>
username:<jsp:getProperty property="username" name="newuser"/><br>
password:<jsp:getProperty property="password" name="newuser"/><br>
email:<jsp:getProperty property="email" name="newuser"/><br>
tel:<jsp:getProperty property="tel" name="newuser"/><br>
address:<jsp:getProperty property="address" name="newuser"/><br>
gender:<jsp:getProperty property="gender" name="newuser"/><br>
</body>
</html>