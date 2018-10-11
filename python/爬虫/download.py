
import urllib.request,urllib.response,http.cookiejar,cookiecutter
from bs4 import BeautifulSoup
url='https://www.cnblogs.com/zdlfb/p/6130724.html'
print('第一种方法')
response=urllib.request.urlopen(url)
print(response.getcode())
print(len(response.read()))
print(response.read())
# print('第二张方法')
# request=urllib.request.request(url)
# request.add_header('user-agent','mozilla/5.0')#爬虫伪装成浏览器
# response1=urllib.request.urlopen(request)
# print(response1.getcode())
# print(len(response1.read()))
# print('第三种方法')
# cj=http.cookiejar
# opener=urllib.build_opener(urllib.HttpCookieProcessor(cj))
# urllib.install_opener(opener)
# response3=urllib.request.urlopen(url)
# print(response3.getcode())
# print(response3.read())
soup=BeautifulSoup()#html文档字符串，html解析器，html文档编码
