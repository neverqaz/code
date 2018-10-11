# -*- coding:utf-8 -*-
import requests
from scrapy.selector import Selector
import MySQLdb
import re
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='article',charset='utf8')
cursor=conn.cursor()
def crawl_ips():
    #爬取西刺的免费ip代理
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/58.0',}
    for page in range(3362):
        resq=requests.get('http://www.xicidaili.com/nn/{0}'.format(page),headers=headers)
        ip_list=[]
        selector=Selector(text=resq.text)
        all_trs=selector.css('#ip_list tr')
        for tr in all_trs[1:]:
            speed_str=tr.css('.bar::attr(title)').extract()[0]
            if speed_str:
                res=re.match('(.*)[\u4E00-\u9FA5]{1}$',speed_str)
                if res:
                    speed =res.group(1)

            all_texts=tr.css('td::text').extract()
            ip=all_texts[0]
            port=all_texts[1]
            proxy_type=all_texts[5]
            ip_list.append((ip,port,proxy_type,speed))
            print(all_texts)
            print(speed)
        for ip in ip_list:
            cursor.execute(
                "insert proxy_ip(ip,port,speed,proxy_type) VALUES('{0}','{1}',{2},'HTTP')ON DUPLICATE KEY UPDATE proxy_type=VALUES(proxy_type)"

                .format(ip[0],ip[1],ip[3])

            )
            conn.commit()


class GetIp(object):
    def delete_ip(self,ip):
        sql="""delete from proxy_ip where ip='{0}'
        
        
        """.format(ip)
        cursor.execute(sql)
        conn.commit()

    def judge_ip(self,ip,port):
        http_url='http://www.baidu.com'
        proxy_url='http://{0}:{1}'.format(ip,port)
        try:
            proxy_dict={
                'http':proxy_url
            }
            response=requests.get(http_url,proxies=proxy_dict)
            return True
        except Exception as e:
            print('invalid ip and port')
            self.delete_ip(ip)
            return False
        else:
            code=response.status_code
            if code >=200 and code<=300:
                print('effective ip')
                return True
            else:
                print('invalid ip and port')
                self.delete_ip(ip)
                return False


    def get_random_ip(self):
        #从数据库当中获取一个随机可用的ip
        sql="""select ip,port from proxy_ip 
                order by rand() 
                limit 1"""
        result=cursor.execute(sql)
        for ip_info in cursor.fetchall():
            ip=ip_info[0]
            port=ip_info[1]
        judge_ip=self.judge_ip(ip,port)
        if judge_ip:
            return 'http://{0}:{1}'.format(ip,port)
        else:
            return self.get_random_ip()
# crawl_ips()
if __name__=='__main__':#写入到main文件里，然后导包就不会执行该语句
    get_ip=GetIp()
    get_ip.get_random_ip()




























