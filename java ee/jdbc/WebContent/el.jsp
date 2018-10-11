<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@taglib uri="http://java.sun.com/jstl/core" prefix="c" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
3+2<br>
<%=3+2 %><br>
<%out.print(3+2);%>
${3+2}<br>
Parameter from login.jsp:
name:${param.name }<br>
age:${param.age}<br>
hahao:${paramValues.hobby[0]},${paramValues.hobby[1]},${paramValues.hobby[2]},<br>
param from session:
${sessionScope.var}

paramValues by forEach:<br>
<c:forEach var="i" items="${paramValues.hobby}">
${i}</c:forEach>

</body>
</html>