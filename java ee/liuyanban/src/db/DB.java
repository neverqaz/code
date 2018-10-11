package db;

import java.sql.*;

import com.mysql.jdbc.*;
import com.mysql.jdbc.Connection;
import com.mysql.jdbc.Statement;

import javabean.User;

public class DB {
	//加载数据库
    String url="jdbc:mysql://localhost:3306/db";//连接字符集
    String user="root";
     String password="123456";
     Connection con=null;//获得连接；
     Statement st=null;//创建容器；
     ResultSet  rs=null;//结果集
 public boolean  conn(String keyword) throws ClassNotFoundException, SQLException{
    	Class.forName("com.mysql.jdbc.Driver"); 
    	con=(Connection) DriverManager.getConnection(url, user, password);//获得连接；
         st=(Statement) con.createStatement();//创建容器；
         if("insert".equals(keyword)){
        	 User u;
        	
        	 
        	 
         }
    return true;}

}
