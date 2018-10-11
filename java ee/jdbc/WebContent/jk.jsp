<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.util.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<% 
List list=(ArrayList)session.getAttribute("data");
Map map;
for(int i=0;i<list.size();i++){
	map=(Map)list.get(i);
	out.print(map.get("id")+","+map.get("name")+","+map.get("password")+"<br>");}%>

</body>
</html>