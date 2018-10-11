<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
 <table border=1><tr><td>key</td><td>VAlUE</td></tr>

<%
Cookie[] cks=request.getCookies();
for(int i=0;i<cks.length;i++){
out.print("<tr><td>"+cks[i].getName()+"</td><td>"+cks[i].getValue()+"</td></tr>");
} %>
</body>
</html>