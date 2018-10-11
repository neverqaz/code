from scrapy.cmdline import execute
import sys
import os
os.path.abspath(__file__)#指的当前python文件
os.path.dirname()#获取当前文件的父目录名
sys.path.append()#调入工程目录这样才使用execte才能生效
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","lagou"])#运行命令scrapy crawl jobbole
# execute(["scrapy","crawl","jobbole"])
