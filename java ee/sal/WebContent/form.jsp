<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>选择商品</title>
<script language="javascript">
var d2=new Date();
var nian=d2.getFullYear().toString();
var yue=d2.getMonth().toString();
var tian=d2.getDate().toString();
var xiaoshi=d2.getHours().toString(); 
var fenzhong=d2.getMinutes().toString();
var miao=d2.getSeconds().toString();
var total=0;//总钱
var j=1;
function writeCookie(bid,tid){	
	var tableq=document.getElementById("tablex");
	var text=document.getElementById(tid).value;
	//alert(nian);
	//alert(yue);
	//alert(tian);
	//alert(xiaoshi);
	//alert(fenzhong);
    var x=0;//商品价格	
	var pert=0;//计算单个商品钱	
	var store='';
	var store1='';	
	var y,m;
	var m=parseInt(bid);
	var d=new Date();
	d.setTime(d.getTime()*60*60*1000);
	for(var i=0;i<3;i++){
	store=tableq.rows[m].cells[i].innerHTML;	
	x=tableq.rows[m].cells[2].innerHTML;//获取商品单价
	store1+="<td>"+encodeURI(store)+"</td>";}
	pert=parseInt(x)*parseInt(text);
	total+=pert;
	//alert("总钱"+total);
	store1+="<td>"+encodeURI(text.toString())+"</td><td>"+pert+"</td><td>"+xiaoshi+"h"+fenzhong+"m"+miao+"s</td>";
	//alert(store1);	
	document.cookie="df"+j+"="+store1+";expires="+d.toString();
	j=j+1;
	//alert("df"+j+"="+store1+";expires="+d.toString());
	alert("添加成功");}
	/*else if(idm==2){
	for(var i=0;i<3;i++){	
	 store=tableq.rows[3].cells[i].innerHTML;
	 x=tableq.rows[3].cells[2].innerHTML;
	 store1+="<td>"+encodeURI(store)+"</td>";}
	 pert=parseInt(x)*parseInt(text2);
	 total+=pert;
	 store1+="<td>"+encodeURI(text2.toString())+"</td><td>"+pert+"</td>";
		document.cookie="df2="+store1+";expires="+d.toString();
		alert("添加成功");}
	 if(idm==3){
	for(var i=0;i<3;i++){	
		store=tableq.rows[4].cells[i].innerHTML;
		x=tableq.rows[4].cells[2].innerHTML;
		store1+="<td>"+encodeURI(store)+"</td>";}
		pert=parseInt(x)*parseInt(text3);
		total+=pert;
		store1+="<td>"encodeURI(text3.toString())+"</td><td>"+pert+"</td>";
	    document.cookie="df3="+store1+";expires="+d.toString();
		alert("添加成功");}
	else if(idm==4){
			for(var i=0;i<3;i++){	
				store=tableq.rows[5].cells[i].innerHTML;
				x=tableq.rows[5].cells[2].innerHTML;
				store1+="<td>"+encodeURI(store)+"</td>";}
			pert=parseInt(x)*parseInt(text4);
			total+=pert;
			store1+="<td>"+encodeURI(text4.toString())+"</td><td>"+pert+"</td>";
				document.cookie="df4="+store1+";expires="+d.toString();}}*/
function tocookie(){
					var d=new Date();
					d.setTime(d.getTime()*60*60*1000);					
                    document.cookie="tap="+total+";expires="+d.toString();
                   }
				
</script>
</head>
<body>
<form action="read.jsp">
<table border=2 align="center" id="tablex">
<th align="center">选择产品 </th>
<tr><td>产品编号</td><td>产品名称</td><td>产品价格</td><td>购买数量</td><td></td></tr>
<tr><td>1</td><td>iphone</td><td>1200</td><td><input type="text"size=2 id="1"></td><td><input type="button"value="加入购物车" onclick="writeCookie('2','1')"></td></tr>
<tr><td>2</td><td>iphonex</td><td>1600</td><td><input type="text"size=2 id="2"></td><td><input type="button"value="加入购物车" onclick="writeCookie('3','2')"></td></tr>
<tr><td>3</td><td>meizu</td><td>1000</td><td><input type="text" size=2 id="3"></td><td><input type="button"value="加入购物车" onclick="writeCookie('4','3')"></td></tr>
<tr><td>4</td><td>oppo</td><td>800</td><td><input type="text" size=2 id="4"></td><td><input type="button"value="加入购物车" onclick="writeCookie('5','4')"></td>
<tr><td>4</td><td>oppo1</td><td>1800</td><td><input type="text" size=2 id="5"></td><td><input type="button"value="加入购物车" onclick="writeCookie('6','5')"></td></tr>
</table>
<br><p align="center"><input type="submit" name="submit" value="submit" onclick="tocookie()" ></p>
</form>
</body>
</html>