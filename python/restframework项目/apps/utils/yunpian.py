
import requests
import json

class YunPian(object):
    def __init__(self,api_key):
        self.api_key=api_key
        self.sigle_send_url='https://sms.yunpian.com/v2/sms/single_send.json'
    def send_sms(self,code,mobile):
        params={
            'apikey':self.api_key,
            'mobile':mobile,
            'text':'[暮雪生鲜]您的验证码是{code}。如非本人操作，请忽略本短信'.format(code=code)


        }

        response=requests.post(self.sigle_send_url,data=params)

        re_dict=json.load(response.text)
        print(re_dict)
        return re_dict

    yun_pain=YunPian("9b11127a9701975c734b8aee81ee3526")
    yun_pain.send_sms("2017","1878543982")
#如果短信发送不成功在云片网设置ip白名单o