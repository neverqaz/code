<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*"%>
    <%  Class.forName("com.mysql.jdbc.Driver");//加载数据库
    String url="jdbc:mysql://localhost:3306/db";//连接字符集
    String user="root";
     String password="123456";
     Connection con=DriverManager.getConnection(url, user, password);//获得连接；
     Statement st=con.createStatement();//创建容器；
     ResultSet  rs=null;//结果集
    String m=request.getParameter("m");
    String id=request.getParameter("id");
    if(m!=null){
    	
    	if(m.equals("1")){
    		rs=st.executeQuery("select *from user where id='"+id+"'");
    		rs.first();
    		st.executeUpdate("insert into user1 values('"+rs.getString("id")+"','"+rs.getString("name")+"','"+rs.getString("password")+"')");
    		st.executeUpdate("delete from user where id='"+id+"'");
    	}
    	if(m.equals("2")){
    		rs=st.executeQuery("select *from user where id='"+id+"'");
    		rs.first();
    		 
    		st.executeUpdate("insert into user values('"+Integer.parseInt(rs.getString("id"))+"','"+rs.getString("name")+"','"+rs.getString("password")+"')");
    		st.executeUpdate("delete from user1 where id='"+id+"'");
    	}
    	
    	
    	
    }
    
    
    
    %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<table border=1>
<caption>user</caption>
<tr><td>编号</td><td>学号</td><td>姓名</td><td>操作</td></tr>
<% 

rs=st.executeQuery("select *from user");//执行查询
 while(rs.next())
	 out.print("<tr><td>"+rs.getString("id")+"</td><td>"+rs.getString("name")+"</td><td>"+rs.getString("password")+"</td><td><a href='index.jsp?id="+rs.getString("id")+"&m=1'>"+">>"+"</a></td></tr>");//结果遍历 
 
 %>
 </table>
 <table border=1>
<caption>user1</caption>
<tr><td>编号</td><td>学号</td><td>姓名</td><td>操作</td></tr>
<% 
   rs=st.executeQuery("select *from user1");//执行查询
 while(rs.next())
	 out.print("<tr><td>"+rs.getString("id")+"</td><td>"+rs.getString("name")+"</td><td>"+rs.getString("password")+"</td><td><a href='index.jsp?id="+rs.getString("id")+"&m=2'>"+"<<"+"</a></td></tr>");//结果遍历 
 rs.close();
 st.close();
 con.close();
 %></table>
</body>
</html>