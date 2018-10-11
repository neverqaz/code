# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#Item 是保存爬取到的数据的容器；其使用方法和python字典类似， 并且提供了额外保护机制来避免拼写错误导致的未定义字段错误。

import scrapy


class HelloItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    type1=scrapy.Field()
    actor=scrapy.Field()
    languge=scrapy.Field()
    time=scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    img=scrapy.Field()
    last_updated = scrapy.Field(serializer=str)