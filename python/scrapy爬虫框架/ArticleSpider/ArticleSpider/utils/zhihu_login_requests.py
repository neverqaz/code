import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
from  PIL import Image
session=requests.session()#用session请求代表requests的某一次请求
session.cookies=cookielib.LWPCookieJar(filename='cookies.txt')
try:
    session.cookies.load(ignore_discard=True)#自动加载已下载好的cookie文件中的值
except:
    print("cookie未加载")
agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
header={

    'HOST':'github.com',
    'referer':'https://github.com/login',
    'USER-Agent':agent

}
def get_authenticity_token():
    response=session.get('https://github.com/login',headers=header)#requests 默认代理python2或者是3所以要设置用户浏览器代理
    result=re.match('.*[\s\S]+?name="authenticity_token"[\s\S]+?value="(.*?)"',response.text)
    if result:
        return result.group(1)
    else:
        return ''
def get_index():#获取主页并下载保存
    response=session.get('https://github.com/',headers=header)
    with open('index_page.html','wb') as f:
        f.write(response.text.encode('utf8'))
    print('ok')
def get_captcha():
    import time
    t=str(int(time.time()*1000))
    captcha_url='https://www.zhihu.com/captcha.gif?r={0}&type=login'.format(t)
    t=session.get(captcha_url,headers=header)#验证码必须使用session才能验证成功因为如果用request将建立新的会话也就对应意味着新session
    with open('captcha.jpg','wb')as f:
        f.write(t.text)
        f.close()
    #打开图片
    try:
        im=Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass
    captcha=input('输入验证码\n>')
    return captcha

def zhihu_login(accout,password):
    #知乎登录

    post_url='https://github.com/session'
    post_data={
            'authenticity_token':get_authenticity_token(),
            'commit':'Sign in',
            'login':accout,
            'password':password,
            'utf8':'&#x2713;',
            #'captcha':get_captcha()
        }
    response_text=session.post(post_url,data=post_data,headers=header)#模拟登录用session的好处就是不用每次requests都需要建立一次链接
    session.cookies.save()
    print(response_text.status_code)
    print(response_text.reason)
zhihu_login('neverqaz','1532105342qaz')
#get_index()
#get_authenticity_token()