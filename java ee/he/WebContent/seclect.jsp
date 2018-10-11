<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String value=request.getParameter("gender");
out.print(value);
if(value.equals("1")){//response.sendRedirect("boy.jsp");//响应内置函数
%>	
<jsp:forward page="boy.jsp"></jsp:forward>
<%	
}
else{//response.sendRedirect("girl.jsp");//响应内置函数
	
	%>	
	<jsp:forward page="girl.jsp"></jsp:forward>//多个表单进行的提交

	<%		
}

%>