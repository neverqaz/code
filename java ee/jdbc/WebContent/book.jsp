<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.sql.*,javax.sql.*,javax.naming.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%  
//事务处理：
DataSource ds=null;
Connection con=null;
     Statement st=null;//创建容器；
     ResultSet  rs=null;//结果集
     try{
    	 Context ctx=new InitialContext();
    	 ds=(DataSource)ctx.lookup("java:comp/env/jdbc/mysql");
    	 con=ds.getConnection();    	 
     }catch(Exception e){e.printStackTrace();}
   if(con!=null){  
	   st=con.createStatement();
     con.setAutoCommit(false);
     try{
     st.executeUpdate("update book set count=count-1 where id='1003'");
     st.executeUpdate("xxxxxinsert into card values('00999','2015122344','1003')");//错误到这跳转到catch语句
     con.commit();
     con.setAutoCommit(true);
     out.print("借书成功");}
     catch(Exception e){
    	 con.rollback();//update语句撤销
    	 out.print("系统异常，完成的语句被撤销");
     }
     st.close();
     con.close();}

     %>
</body>
</html>