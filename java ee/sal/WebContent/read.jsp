<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>购物车</title>
<script>
/*function deletec(name) 
{ 
    var exp = new Date(); 
    exp.setTime(exp.getTime()-100000); 
    
        document.cookie=name+"=   ;expires="+exp.toGMTString(); 
} */
function readcookie(name){
var s;
	
	if (document.cookie.length>0)
	  {
	  c_start=document.cookie.indexOf(name+"=")
	  if (c_start!=-1)
	    { 
	    c_start=c_start+name.length+1 
	    c_end=document.cookie.indexOf(";",c_start)
	    if (c_end==-1) c_end=document.cookie.length
	    s=document.cookie.substring(c_start,c_end);
	    alert("一共消费"+s+"元哦，哈哈哈哈"); 
	    } 
	  }
	
	
	
	
}
</script>
</head>
<body>
 <table border=1 align="center">
<th>购物车</th>

<tr><td>产品编号</td><td>产品名称</td><td>产品价格</td><td>购买数量</td><td>商品总值</td><td>添加的时间</td></tr>
<%
Cookie[] cks=request.getCookies();
String s,n;
for(int i=0;i<cks.length;i++){
	s=cks[i].getName();	
	n=cks[i].getValue();
	
	if(!s.equals("tap")){
out.print("<tr>"+n);}} 
%></table>
<br><p align="center"><input type="button"value="结算"onclick="readcookie('tap')">&nbsp;&nbsp;<input type="button"  value="返回" onclick="location.href='form.jsp'"></p>
</body>
</html>