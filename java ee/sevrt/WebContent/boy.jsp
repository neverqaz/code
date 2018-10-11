<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>boy</title>
</head>
<body bgcolor="blue"> <h1>welcom boy</h1>

<%
String currentuser=null;
//读session
String s=(String)session.getAttribute("user");
if(s!=null){currentuser=s;}
//读cookie
Cookie[] cks=request.getCookies();
if(null!=cks){
	
	for(int i=0;i<cks.length;i++){
		
		if("user".equals(cks[i].getName())){
			
			currentuser=cks[i].getValue();
		}
	}
	
}

if(currentuser==null){
	out.print("你还没有登陆，请点击<a href='login.html'>这里登陆</a>");
	
}else{ 
	out.println("您好"+s);
	out.println("<h1>成功</h1>");
out.println("<a href='girl.jsp' >link1</a>");
} 
%>

</body>
</html>