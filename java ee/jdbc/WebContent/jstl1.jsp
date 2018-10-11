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
<%
String s=(String)session.getAttribute("user");
 out.print(s);%>
<c:choose>
<c:when test="${!empty(sessionScope.user)}">hello</c:when>
<c:otherwise> please login in</c:otherwise>


</c:choose>
</body>
</html>