<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%! int i=0; %>//变量声明
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>index</title>
</head>
<body>
<%=i %>//变量的使用
Date d=new Date();
out.print("<font color='red'>"+d.toString()+"</font>");
//<%@include file="hello.jsp" %>//复制粘贴到源代码include 指令包含源码
//jsp动作标签
<jsp:include page="hello.jsp">//hello.jsp这个的运行结果包含进来
<jsp:param value="hello" name="school"/>//包含页面同时传参数

</jsp:include>

</body>
</html>