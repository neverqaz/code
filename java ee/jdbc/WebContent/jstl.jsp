<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<c:if test="${!empty(sessionScope.user)}">
用户名：<br>
${sessionScope.user}<br>
<h1>hello</h1>
<c:out value="${sessionScope.var}"></c:out></c:if>
 <%
/*String s=(String)session.getAttribute("user");
if(s!=null){
	out.print("hello");
}*/
%>
List content:
<table border="1">
<tr><td>ID</td><td>name</td><td>password</td></tr>
<c:forEach var="i" items="${sessionScope.data}">
<tr><td>${i.id}</td><td>${i.name}</td><td>${i.password }</td></tr></c:forEach></table>
<c:forEach var="i" begin="1" end="10" step="1">${i}</c:forEach>
</body>
</html>