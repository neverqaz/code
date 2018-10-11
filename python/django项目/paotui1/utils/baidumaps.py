# -*- coding: utf-8 -*-
import requests
import urllib.parse
import json
"""
跑腿费用相关计算：
1.第三方购买费(purchase)：由发单方填写。
2.跑腿费(run_money)：根据接单后所生成的路程距离（distance）×单路程距价钱
3.单路程距离费（distancemoney）：1米多少钱：
            根据丰泰餐厅（111.723332,40.812727）到C座（111.721962,40.812365）,
            带一次饭的实际钱是1.5元算出： 
            根据算路线距离接口得出：distance=115米 耗时98秒
 所以路程距离费(distancemoney)=0.01304348(元/米)
4.手续费(tax)：收取跑腿费的10%（按最短距离算1.5元×0.1=0.15元）
5.总费用(order_total):order_total=distance×distancemoney+distance×distancemoney×0.1+purchase            
                     order_total=distance×distancemoney×1.1+purchase

"""
class BAIDUMAPS(object):
     distancemoney=0.01304348#1米多少钱
     handle_tax=0.1#手续费的利率10%

     def __init__(self):
         self.ak="unrcs1AVyGvK5Y085KID6mBmkrK62Dmw"
     # def getlocation(self):
     #     """利用坐标定位
     #     缺点：只能定位到市级单位
     #     """
     #     url = "http://api.map.baidu.com/location/ip"
     #     requset_url="{url}?ak={ak}&coor=bd09ll".format(url=url,ak=self.ak)
     #     result=requests.get(requset_url).text.encode("utf-8").decode('unicode_escape')
     #     return result
     def calulation_distance(self,origin,destination,mode,region):
         dict1={"mode":mode,"origin":origin,"destination":destination,"output":"json","region":region,"ak":self.ak}
         data=urllib.parse.urlencode(dict1)
         url="http://api.map.baidu.com/direction/v1?{data}".format(data=data)
         response=requests.get(url).json()#.text.encode("utf-8").decode('unicode_escape')
         #结果在result里的distance（距离较短）(米)，duration（耗时）（秒）
         distance=float(response["result"]["routes"][0]["distance"])
         duration=response["result"]["routes"][0]["duration"]
         if distance==0:
             run_money=0
             tax=0
         elif distance<=1000 and distance>0:
             run_money=2
             tax = run_money * self.handle_tax  # 手续费
         elif distance<=3000 and distance>1000:
             run_money=4
             tax = run_money * self.handle_tax
         else :
             run_money=4+(distance-3000)/1000*1
             tax = run_money * self.handle_tax


         # run_money=distance*self.distancemoney#跑腿费
         # tax=run_money*self.handle_tax#手续费
         dict2={"distance":distance,"duration":duration,"run_money":run_money,"tax":tax}
         return dict2
     def gps_follow(self,origin,origin_name
                    ,destination,destination_name,
                    mode,region):
        """
        地图导航
        :param origin: 起点
        :param origin_name: 起点名
        :param destination: 终点
        :param destination_name: 
        :param mode: 导航模式为三种：transit、driving、walking
        :param region: 城市名或县名（当给定region时，认为起点和终点都在同一城市，除非单独给定起点或终点的城市。）
        :param origin_region:
        :param destination_region：
        :return: 
        """
        origin1="latlng:{origin}|name:{origin_name}".format(origin=origin,origin_name=origin_name)
        destination1="latlng:{destination}|name:{destination_name}".format(destination=destination,destination_name=destination_name)
        dict1={"origin":origin,"destination":destination,"mode":mode,"region":region,"output":"html","src":"webapp.baidu.openAPIdemo"}
        data=urllib.parse.urlencode(dict1)
        url="http://api.map.baidu.com/direction?{data}".format(data=data)

        return url
if __name__=="__main__":
    """
    #ip定位测试
    ip=BAIDUMAPS().getlocation()
    print(ip)"""
    """
    #导航测试
    origin = "40.812727,111.723332"
    origin_name="送货"
    destination = "40.812365,111.721962"
    destination_name="收货"
    mode="walking"
    region="呼和浩特市"
    b = BAIDUMAPS().gps_follow(origin=origin, origin_name=origin_name, destination=destination,
                               destination_name=destination_name, mode=mode, region=region)
    print(b)"""
    origin = "40.812727,111.723332"
    destination = "40.812365,111.721962"
    region = "呼和浩特市"
    mode="walking"
    a=BAIDUMAPS().calulation_distance(origin=origin,destination=destination,mode=mode,region=region)
    distance=a.get("distance","")
    duration=a.get("duration","")
    print("根据经纬度坐标由丰泰餐厅到内蒙古农业大学c座：距离为：{distance}米，耗时：{duration}秒".format(distance=distance,duration=duration))
    #http://api.map.baidu.com/marker?location=111.66035052,40.82831887&title = 我的位置&content=百度奎科大厦&output=html&src=webapp.baidu.openAPIdemo
    #http://api.map.baidu.com/geocoder/v2/?address = 呼和浩特市赛罕区内蒙古农业大学&output =json&ak=unrcs1AVyGvK5Y085KID6mBmkrK62Dmw&callback=showLocation"""