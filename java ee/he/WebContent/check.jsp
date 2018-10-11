<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% String name=request.getParameter("name");
String password=request.getParameter("password");
if(name.equals(password)){
	response.sendRedirect("boy.jsp");
	session.setAttribute("user", name);
	Cookie ck=new Cookie("user",name);
	ck.setMaxAge(1200);
	response.addCookie(ck);

	
}else response.sendRedirect("login.html");

%>