# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import ArticleItem,ArticleItemLoader
from ArticleSpider.utils.common import get_md5
import os
import datetime
from scrapy.loader import ItemLoader#易于后期的维
from  selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher#分发器
from scrapy import signals
# class get_image_url:
#     def __init__(self, image_path):
#         self.image_path = image_path
#     @classmethod
#     def from_setting(cls, settings):
#         image_path = settings['IMAGES_STORE']
#         return cls(image_path)
class JobboleSpider(scrapy.Spider):

    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']
    # def __init__(self):
    #     self.browser=webdriver.Firefox()
    #     super(JobboleSpider,self)
    #     dispatcher.connect(self.spider_closed,signals.spider_closed)#信号量的使用
    # def spider_closed(self,spider):
    #     #当爬虫退出的时候关闭firefox
    #     print("spider closed")
    #     self.browser.quit()
    #收集伯乐在线所有404的url以及404的页面数
    handle_httpstatus_list=[404]

    def __init__(self):
        self.fail_urls=[]
        dispatcher.connect(self.handle_spider_closed, signals.spider_closed)

    def handle_spider_closed(self,spider,reasion):
        self.crawler.stats.set_value('failed_urls',','.join(self.fail_urls))
        pass


    def parse(self, response):

        if response.status==404:
            self.fail_urls.append(response.url)
            self.crawler.stats.inc_value('fail_urls')#遇到404的url就加1

        '''

        1.获取文章列表页中的文章url并交给scrapy下载器进行解析（解析函数进行具体字段的解析）
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse函数'''
        #解析列表页所有文章的url并交给scrapy下载器进行解析、
        nodes_url=response.css('#archive .floated-thumb .post-thumb a')
        for node_url in nodes_url:
            image_url=node_url.css('img::attr(src)').extract_first("")
            post_url=node_url.css("::attr(href)").extract_first("")
            #meta属性是往指定函数传递想要的字段
            yield Request(url=parse.urljoin(response.url,post_url),meta={"format_image":image_url},callback=self.parse_detail)#parse.urljoin(获取当前网页的域名,当前链接不完整的部分域名)
           #yield 是交个scrapy下载的关键字
            # print(p)
        #提取下一页url交给scrapy下载
        #extract_first(“ ”)函数指定默认为空格
        next_url=response.css('.next.page-numbers::attr(href)').extract_first(" ")#.next.page-numbers中间没有空格代表俩个同时指向同一个标签<a class="next page-numbers" href='#'>
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url), callback=self.parse)



    def parse_detail(self,response):

    #     #提取文章的具体字段
    #     #/html/body/div[3]/div[3]/div[1]/div[1](div[3]的下标从1开始)
        front_image_url=response.meta.get('format_image','')#文章封面图
    #     title=response.xpath('//*[@class="entry-header"]/h1/text()').extract()#id是唯一表示
    #     post_time=response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·',' ').strip()#extract()表示把它变为一个列表访问下表为‘0’的元素，strip（）是去掉空格换行,replace('需要替换的内容'，‘替换成的内容’)
    #     praise_nums=int(response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0])#contains()函数表示span标签中的class属性的内容包含vote-post-up
    #     fav_nums=response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
    #     result=re.match('.*(\d+).*',fav_nums)
    #     if result:
    #         fav_nums=int(result.group(1))
    #     else :
    #         fav_nums=0
    #     comment_nums = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
    #     result = re.match('.*(\d+).*',comment_nums)
    #     if result:
    #         comment_nums = int(result.group(1))
    #     else:
    #         comment_nums=0
    #     context=response.xpath('//div[@class="entry"]').extract()[0]
    #     tag_list=response.xpath('//*[@id="post-114253"]/div[2]/p/a/text()').extract()
    #     tag_list=[element for element in tag_list  if not element.strip().endswith('Git')]#去掉以前获取过的元素Git重复(不以Git为结尾的过滤掉)列表生成器
    #     #列表生成器过程：1.定义elemet 2.判断if not 结果为真时赋值给element,3.element添加列表中
    #     tags=','.join(tag_list)
    #     #往item当中填值
    #     '''  title=scrapy.Field()
    # post_time=scrapy.Field()
    # url=scrapy.Field()
    # url_object_id=scrapy.Field()
    # front_image_url=scrapy.Field()
    # front_image_path=scrapy.Field()
    # praise_nums=scrapy.Field()
    # comment_nums=scrapy.Field()
    # fav_nums=scrapy.Field()
    # tags=scrapy.Field()
    # content=scrapy.Field()'''
    #     article = ArticleItem()
    #     article['url_object_id']=get_md5(response.url)
    #     article['title']=title
    #     try:
    #         post_time=datetime.datetime.strptime(post_time,'%Y/%m/%d').date()
    #     except Exception as e:
    #         post_time=datetime.datetime.now()
    #     article['post_time']=post_time
    #     article['url']=response.url
    #     article['front_image_url']=[front_image_url]#下载图片的路径传递的是数组
    #     article['praise_nums']=praise_nums
    #     article['fav_nums']=fav_nums
    #     article['comment_nums']=comment_nums
    #     article['tags']=tags
    #     article['content']=context
    #     yield article#调用yield article会传递到pipelines.py 中
    #     #通过css选择器提取字段
    #     # title1=response.css('.entry-header h1::text').extract()[0]
    #     # post_time1=response.css('p.entry-meta-hide-on-mobile::text').extract()[0].strip().replace('·',' ').strip()
    #     # praise_nums1=int(response.css('.vote-post-up h10::text').extract()[0])
    #     # fav_nums=response.css('.bookmark-btn::text').extract()[0]
    #     # result = re.match('.*?(\d+).*', fav_nums)
    #     # if result:
    #     #     fav_nums = int(result.group(1))
    #     # else:
    #     #     fav_nums=0
    #     # comment_nums=response.css('a[href="#article-comment"] span::text').extract()[0]
    #     # result = re.match('.*?(\d+).*', comment_nums)
    #     # if result:
    #     #     comment_nums = int(result.group(1))
    #     # else:
    #     #     comment_nums=0
#通过item Loader加载item
        front_image_url = response.meta.get('format_image', '')  # 文章封面图
        item_loader=ArticleItemLoader(item=ArticleItem(),response=response)#ArticleItemLoader是自定义的itemloader，他是继承itemloader，是在item.py文件重写的
        item_loader.add_css('title','.entry-header h1::text')
        item_loader.add_css('post_time','p.entry-meta-hide-on-mobile::text')
        item_loader.add_value('url',response.url)
        item_loader.add_value('url_object_id',get_md5(response.url))
        item_loader.add_value('front_image_url',[front_image_url])
        item_loader.add_css('praise_nums','.vote-post-up h10::text')
        item_loader.add_css('fav_nums','.bookmark-btn::text')
        item_loader.add_css('comment_nums','a[href="#article-comment"] span::text')
        item_loader.add_css('tags','p.entry-meta-hide-on-mobile a::text')
        item_loader.add_css('content','div.entry')
        article=item_loader.load_item()#利用item loader生成item
        yield article









