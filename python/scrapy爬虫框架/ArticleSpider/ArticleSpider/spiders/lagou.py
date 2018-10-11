# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ArticleSpider.items import LagouJobItem,LagouJobItemLoader
from ArticleSpider.utils.common import get_md5
import datetime
class LagouSpider(CrawlSpider):#继承CrawlSpider
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']
    rules = (
        Rule(LinkExtractor(allow=('zhaopin/.*',)),follow=True),
        Rule(LinkExtractor(allow=('gongsi/j\d+.html',)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'),callback='parse_job', follow=True),
    )#allow=是允许提取的字段，deny=是要舍弃的字段，allowed_domains=是在这个域名之下的提取，deny_domains=是在这个域名之下的抛弃，restrict_xpaths=自定义xpath
#tags=('a','area'),attrs=('href')默认是从a标签中herf提取url，restrict_css自定义css选取规则
    # def parse_start_url(self, response):
    #     return []
    #
    # def process_results(self, response, results):
    #     return results

    def parse_job(self, response):
        #解析拉勾网的职位
        item_loader=LagouJobItemLoader(item=LagouJobItem(),response=response)
        item_loader.add_css('title','.job-name::attr(title)')
        item_loader.add_value('url',response.url)
        item_loader.add_value('url_object_id',get_md5(response.url))
        item_loader.add_css('salary','.salary::text')
        item_loader.add_xpath('job_city','//*[@class="job_request"]/p/span[2]/text()')
        item_loader.add_xpath('work_years', '//*[@class="job_request"]/p/span[3]/text()')
        item_loader.add_xpath('degree_need', '//*[@class="job_request"]/p/span[4]/text()')
        item_loader.add_xpath('job_type', '//*[@class="job_request"]/p/span[5]/text()')
        item_loader.add_css('tags','.position-label li::text')
        item_loader.add_css('publish_time','.publish_time::text')
        item_loader.add_css('job_advantage','.job-advantage p::text')
        item_loader.add_css('job_desc', '.job_bt div')
        item_loader.add_css('job_addr','.work_addr')
        item_loader.add_css('company_name','#job_company dt a img::attr(alt)')
        item_loader.add_css('company_url', '#job_company dt a::attr(href)')
        item_loader.add_value('crawl_time',datetime.datetime.now())
        job_item=item_loader.load_item()
        return job_item


