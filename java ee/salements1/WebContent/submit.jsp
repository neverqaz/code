<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String button1=(String)request.getParameter("button");
Cookie ck=new Cookie("1",button1);

ck.setMaxAge(3600);
response.addCookie(ck);
%>


