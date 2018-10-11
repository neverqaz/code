<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*,javax.sql.*,javax.naming.*,java.util.*" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<% Context ctx=new InitialContext();
DataSource ds=(DataSource)ctx.lookup("java:comp/env/jdbc/mysql");
Connection con=ds.getConnection();
Statement st=con.createStatement();
ResultSet rs=st.executeQuery("select *from user");
List<Map<String,String>> list=new ArrayList<Map<String,String>>();
Map<String,String> map;
while(rs.next()){
	map=new HashMap<String,String>();
	map.put("id", rs.getString("id"));
	map.put("name", rs.getString("name"));
	map.put("password", rs.getString("password"));
	list.add(map);
}
session.setAttribute("data",list);


rs.close();
st.close();
con.close();
response.sendRedirect("jstl.jsp");

%>
</body>
</html>