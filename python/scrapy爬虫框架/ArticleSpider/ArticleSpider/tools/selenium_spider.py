from selenium import webdriver
from scrapy.selector import Selector
browser=webdriver.Firefox()
import time
# browser.get('https://item.taobao.com/item.htm?id=574542211641&ali_refid=a3_430673_1006:1108210308:N:%E5%A5%B3%E8%A3%85:7902cc3b92b7fea49f1403b15d829473&ali_trackid=1_7902cc3b92b7fea49f1403b15d829473&spm=a2e15.8261149.07626516002.1')
# print(browser.page_source)
# selector=Selector(text=browser.page_source)
# price=selector.css('.tb-rmb-num::text')
#模拟知乎登录
browser.get('https://www.zhihu.com/signup?next=%2F')
browser.find_element_by_css_selector('.SignContainer-switch span').click()
browser.find_element_by_css_selector('.Login-content input[name="username"]').send_keys('18548019624')
browser.find_element_by_css_selector('.Login-content input[name="password"]').send_keys('1532105342qaz')
browser.find_element_by_css_selector('button.SignFlow-submitButton').click()
print(browser.page_source)
#selenium 完成微博登录
# browser.get('https://weibo.com')

# time.sleep(15)
# browser.find_element_by_css_selector('#loginname').send_keys('18548019624')
# browser.find_element_by_css_selector('.info_list.password input[name="password"]').send_keys('1532105342qaz')
# browser.find_element_by_css_selector('.info_list.login_btn a[node-type="submitBtn"]').click()
# time.sleep(15)
# browser.find_element_by_css_selector('a[title="iPhone/iPad"]').click()
# browser.find_element_by_css_selector('.home.S_txt1 .S_txt1').click()
# time.sleep(15)
#自动下拉
# browser.get('https://www.oschina.net/blog')
# time.sleep(5)
# for i in range(3):
#   browser.execute_script('window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage')
#   time.sleep(3)

#如何chormedirver不加载图片
# chorme_opt=webdriver.ChromeOptions()
# pref={"profile.managed_default_content_settings.images":2}
# chorme_opt.add_experimental_option('prefs',pref)
# browser=webdriver.Chrome(chrome_options=chorme_opt)
#firefox不加载图片
# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference('permissions.default.image', 2)
# # firefox_profile.set_preference('browser.migration.version', 9001)#部分需要加上这个
# # #禁用css
# # firefox_profile.set_preference('permissions.default.stylesheet', 2)
# # #禁用flash
# # firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# # #禁用js
# # firefox_profile.set_preference('javascript.enabled', 'false')
# browser = webdriver.Firefox(firefox_profile=firefox_profile)
# browser.get('https://www.taobao.com')
#phantomjs,是一个无界面的浏览器，多进程的情况下phantomjs性能下降严重
# browser=webdriver.PhantomJS(executable_path='/usr/bin/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
# browser.get('https://item.taobao.com/item.htm?id=574542211641&ali_refid=a3_430673_1006:1108210308:N:%E5%A5%B3%E8%A3%85:7902cc3b92b7fea49f1403b15d829473&ali_trackid=1_7902cc3b92b7fea49f1403b15d829473&spm=a2e15.8261149.07626516002.1')
# print(browser.page_source)
# browser.quit()













#browser.quit()