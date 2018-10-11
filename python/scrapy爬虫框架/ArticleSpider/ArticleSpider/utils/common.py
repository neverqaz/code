
import hashlib
import re
def get_md5(url):
    if isinstance(url,str):#python3当中所有编码都是unicode，unicode是不能进行hash的
        url=url.encode('utf-8')#改编码为utf-8
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()
def extract_nums(text):
    #从字符串中提取数字
    result = re.match('.*(\d+).*', text)
    if result:
        nums = int(result.group(1))
    else:
        nums = 0
    return nums