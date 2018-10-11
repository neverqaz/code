// 百度地图API功能
	function G(id) {
		return document.getElementById(id);
	}

	var map = new BMap.Map("l-map");
	map.centerAndZoom("赛罕区",12);
	map.enableScrollWheelZoom();   //启用滚轮放大缩小，默认禁用
	map.enableContinuousZoom();    //启用地图惯性拖拽，默认禁用                   // 初始化地图,设置城市和地图级别。


	var ac = new BMap.Autocomplete(    //建立一个自动完成的对象
		{"input" : "suggestId"
		,"location" : map
	});

	ac.addEventListener("onhighlight", function(e) {  //鼠标放在下拉列表上的事件
	var str = "";
		var _value = e.fromitem.value;
		var value = "";
		if (e.fromitem.index > -1) {
			value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
		}
		str = "FromItem<br />index = " + e.fromitem.index + "<br />value = " + value;

		value = "";
		if (e.toitem.index > -1) {
			_value = e.toitem.value;
			value = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
		}
		str += "<br />ToItem<br />index = " + e.toitem.index + "<br />value = " + value;
		G("searchResultPanel").innerHTML = str;
	});

	var myValue;
	ac.addEventListener("onconfirm", function(e) {    //鼠标点击下拉列表后的事件


	var _value = e.item.value;
		myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
		G("searchResultPanel").innerHTML ="onconfirm<br />index = " + e.item.index + "<br />myValue = " + myValue;

		setPlace();
	});

	function setPlace(){
		map.clearOverlays();    //清除地图上所有覆盖物
		function myFun(){

			var pp = local.getResults().getPoi(0).point;    //获取第一个智能搜索的结果
			map.centerAndZoom(pp, 18);
			map.addOverlay(new BMap.Marker(pp));    //添加标注

		}



		var local = new BMap.LocalSearch(map, { //智能搜索

		  onSearchComplete: myFun,
          renderOptions: {map: map}//, panel: "r-result1"}

		});
		local.search(myValue);

	}

var geoc = new BMap.Geocoder();
var b=myValue;
map.addEventListener("click",function(e){
                        var myValue1=b;
			map.clearOverlays();
			var new_point = new BMap.Point(e.point.lng,e.point.lat);
			var marker = new BMap.Marker(new_point);  // 创建标注
			map.addOverlay(marker);              // 将标注添加到地图中
			map.panTo(new_point);
             	        var pt = e.point;
		geoc.getLocation(pt, function(rs){
           if(null==b){
                                              //rs.address
                         //re.surroundingPois["title"]

                     // var tag=allPois[0].tags

		//var b=confirm(pt.lng + "," + pt.lat)//+","+allPois[1].title+",address:"+allPois[1].address);

			var addComp = rs.addressComponents;
                        var allPois = rs.surroundingPois;
                       myValue1=addComp.province + addComp.city+addComp.district +addComp.street +addComp.streetNumber+allPois[0].title;}
                       city=addComp.city;
                       address=prompt("请确认您的地址信息并补充完整：",myValue1); // 弹出input框

                      if(null!=address){window.location.href="/map_return?point="+pt.lat + "," +pt.lng+"&address="+address+"&city="+city;}
	             else{
		    alert("请重新选取您的位置");
                        myValue1=null;
                        b=null;

                           }
});
	});
