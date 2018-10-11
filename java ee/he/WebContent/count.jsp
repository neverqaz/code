<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
int count; 
out.println(application.getAttribute("count"));
if(null==application.getAttribute("count")){
	count=1;
}else{
   count=(int)application.getAttribute("count");
   count++;
   
}
application.setAttribute("count", count);
out.println("你是第"+count+"访问人");
%>