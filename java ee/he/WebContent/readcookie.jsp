<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
/*function ctt(){
	var d2=new Date();
	var nian=d2.getYear();
	var yue=d2.getMonth();
	var tian=d2.getDay();
	var xiaoshi=d2.getHours(); 
	var fenzhong=d2.getMinutes();
	var miao=d2.getSeconds();
	var s=nian.toString()+"."+yue.toString()+"."+tian.toString()+"/"+xiaoshi.toString()+":"+fengzhong.toString()+":"+miao.toString();
	alert(s);
	return s;
}*/
<body>
<%
Cookie[] cks=request.getCookies();
if(null!=cks){
	
	for(int i=0;i<cks.length;i++){
		
		if("user".equals(cks[i].getName())){
			
			out.println(cks[i].getValue());
		}
	}
	
}


%>
</body>
</html>