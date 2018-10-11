
#Spider是用户编写用于从单个网站(或者一些网站)爬取数据的类。
# 其包含了一个用于下载的初始URL，如何跟进网页中的链接以及如何分析页面中的内容， 提取生成 item 的方法。
#
# 为了创建一个Spider，您必须继承 scrapy.Spider 类， 且定义以下三个属性:
#
# name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
# start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取。
# parse() 是spider的一个方法。 被调用时，
# 每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
# 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。

import scrapy
from hello.items import HelloItem
class JMeterVersionSpider(scrapy.Spider):
    name = 'JMeterVersion'   #爬虫的名字
    url='http://www.80s.tw'
    start_urls = [
        'http://www.80s.tw/']  #要爬取的网站列表

    #def parse(self, response):
            # for sel in response.xpath('//ul/li'):
                # item = HelloItem()
                # item['title'] = sel.xpath('a/text()').extract()
                # item['link'] = sel.xpath('a/@href').extract()
                # item['desc'] = sel.xpath('text()').extract()
                # yield item
    # def parse(self, response):
    #         self.log('A response from %s just arrived!' % response.url)


    # def start_requests(self):
    #     return [scrapy.FormRequest("http://www.example.com/login",
    #                                formdata={'user': 'john', 'pass': 'secret'},
    #                                callback=self.logged_in)]
    #
    # def logged_in(self, response):
    #     # here you would extract links to follow and return Requests for
    #     # each of them, with another callback
    #     pass
    def parse(self, response):
        sel = scrapy.Selector(response)
        print (response.body)
        for h3 in sel.xpath('//h3').extract():
            for a in sel.xpath('//h3/a/@href').extract():
                a =self.url+a
                yield scrapy.Request(a)  # meta={'dont_redirect':True}
                # title = scrapy.Field()
                # type1 = scrapy.Field()
                # actor = scrapy.Field()
                # languge = scrapy.Field()
                # time = scrapy.Field()
                # link = scrapy.Field()
                # desc = scrapy.Field()
                # img = scrapy.Field()
                # last_updated = scrapy.Field(serializer=str)
                h1=sel.xpath('//h1/text()').extract()
                type=sel.xpath('//span[@class="span_block"]/a/text()').extract()
                actor=sel.xpath('//*[@id="minfo"]/div[2]/span[4]/span/a/text()').extract()
                desc=sel.xpath('//*[@id="movie_content"]/text()[1]').extract()
                link=sel.xpath('//*[@id="myform"]/ul/li[2]/span[2]/a/@href').extract()
                #languge=sel.xpath('//')
                yield HelloItem(title=h1,type1=type,actor=actor,desc=desc,link=link)


             # print(h3)
        # for li in response.xpath('//li').extract():
        #     li=self.url+li
        #     yield scrapy.Request(li, callback=self.parse)
        # for urls in sel.xpath('//a/@href').extract():
        #      urls=self.url+urls
        #      yield scrapy.Request(urls, callback=self.parse)


            #print(url)
