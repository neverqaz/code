from .md5 import get_md5
import requests
import datetime
class MiaoDiYun(object):
    def __str__(self):
        self.accountSid="235d31100b334183ad130eb55d873534"#开发者主账号ID
        self.templateid="700853080"#短信模板id
        self.url="https://api.miaodiyun.com/20150822/affMarkSMS/sendSMS"
        #self.sig#MD5(ACCOUNT SID + AUTH TOKEN + timestamp)。共32位（小写）
        self.AUTH_TOKEN="f48f5a54c5ba44fb95c304d273eceff4"
        self.header={"Content-type:application/x-www-form-urlencoded"}
    def send_message(self,mobile,send_name,accpet_name):
         param='{send_name},{accpet_name},{mobile}'.format(send_name=send_name,accpet_name=accpet_name,mobile=mobile)#亲爱的{1}：您发的订单 ，{2}接单了，电话为:{3}，请尽快核实，请您尽快到个人中心付款，么么哒！
         timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         to=mobile
         sig=get_md5("{1}{2}{3}".format(self.accountSid,self.AUTH_TOKEN,timestamp))#MD5(ACCOUNT SID + AUTH TOKEN + timestamp)。共32位（小写）
         send_param={
             "accountSid":self.accountSid,
             "templateid":self.templateid,
             "param":param,
             "to":to,
             "timestamp":timestamp,
             "sig":sig}
         requests.post(url=self.url,data=send_param,headers=self.header)
if __name__=="__main__":
    m=MiaoDiYun()
    m.send_message("18810819842","宋有利","渠美丽")