<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
 <%  Class.forName("com.mysql.jdbc.Driver");//加载数据库
    String url="jdbc:mysql://localhost:3306/db";//连接字符集
    String user="root";
     String password="123456";
     Connection con=DriverManager.getConnection(url, user, password);//获得连接；
     Statement st=con.createStatement();//创建容器；
     ResultSet  rs=null;//结果集
     DatabaseMetaData dmd=con.getMetaData();
     out.print("1.数据库的基本信息：<br>");
     out.print(dmd.getURL()+"<br>");
     out.print(dmd.getDatabaseProductName()+"<br>");
     out.print(dmd.getDriverName()+"<br>");
     out.print(dmd.getUserName()+"<br>");
      rs=dmd.getTables(con.getCatalog(), "root", null,new String[]{"table"});//ResultSet类型
      out.print("2.表名：<br>");
    while(rs.next()){
    	out.print(rs.getString("table_name")+"<br>");
    }
      rs=st.executeQuery("select *from user");//项目不要用select*
      ResultSetMetaData rsmd=rs.getMetaData();
      out.print("3.表的列数：");
      out.print("columns="+rsmd.getColumnCount()+"<br>");
      out.print("4.表的数据类型：<br>");
      for(int i=1;i<=rsmd.getColumnCount();i++){
    	  out.print(rsmd.getColumnName(i)+":"+rsmd.getColumnType(i)+":"+rsmd.getColumnTypeName(i)+"<br>");
    	  
      }
      rs.close();
      //数据库事务是操作的集合（1.原子性：不可分割要么全部完成，要么均不执行{回滚（撤销）}2.一致性3.隔离性4持久性）commit(),rollback();
      
     %>
</body>
</html>