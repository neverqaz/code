# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#定义数据的保存格式
import scrapy,re
import datetime
from w3lib.html import remove_tags
from scrapy.loader.processors import MapCompose#可以传递任意多的预处理函数
from scrapy.loader.processors import TakeFirst,Join#提取list数组当中的第一个元素
from scrapy.loader import ItemLoader
from ArticleSpider.settings import SQL_DATE_FORMAT,SQL_DATETIME_FORMAT
from ArticleSpider.utils.common import extract_nums
class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
def add_jobbole(value):
    return value + 'jobbole'


def date_coverse(value):
    try:
        post_time = datetime.datetime.strptime(value,'%Y/%m/%d').date()
    except Exception as e:
        post_time = datetime.datetime.now()
    return post_time
class ArticleItemLoader(ItemLoader):#重载itemloader类
    #自定义itemloader
    default_output_processor =TakeFirst()#因为示意itemloader所生成的item是以list存储的，所以提取list数组当中的第一个元素进行输出（str）
def get_nums(values):
    result = re.match('.*(\d+).*', values)
    if result:
        nums = int(result.group(1))
    else:
        nums = 0
    return nums
def remove_comment_tags(value):
    #去tags中提取的评论
    if '评论' in value:
        return ''
    else:
        return value
def return_value(value):
    return value
class ArticleItem(scrapy.Item):
    title=scrapy.Field(
        # title 传递进来进行预处理
        #imput_processor=MapCompose(lambda x:x+'bbbbbxy',add_jobbole)#lambda函数（拉不大函数）
    )
    post_time=scrapy.Field(
        input_processor=MapCompose(date_coverse)
    )
    url=scrapy.Field()
    url_object_id=scrapy.Field()#使我们的url变为长度固定的唯一值
    front_image_url=scrapy.Field(
        #在setting当中下载图片到本地时配置图片来源url代表是一个list，而自定义ArticleItemLoader默认的变为了str类型所以要写一个函数来覆盖掉默认str
        #在sql语句当中改为取front_image_url[0]
        output_processor=MapCompose(return_value)
    )
    front_image_path=scrapy.Field()
    praise_nums=scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums=scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums=scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags=scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(',')#把该list变为str类型并用‘,’号连接起来
    )
    content=scrapy.Field()
    def get_insert_sql(self):
        insert_sql = """insert into article(title,post_time,url,url_object_id,
        front_image_url,front_image_path,praise_nums,comment_nums,fav_nums,tags,content)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """

        params=(self['title'], self['post_time'], self['url'], self['url_object_id'], self['front_image_url']
                        , self['front_image_path'], self['praise_nums'],
                        self['comment_nums'], self['fav_nums'], self['tags'], self['content'])
        return insert_sql,params
class ZhihuQuestionItem(scrapy.Item):
    #知乎问题item
    zhihu_id=scrapy.Field()
    topics=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    answer_num=scrapy.Field()
    comment_num=scrapy.Field()
    watch_user_num=scrapy.Field()
    click_num=scrapy.Field()
    crawl_time=scrapy.Field()
    def get_insert_sql(self):
        insert_sql="""
            insert into zhihu_question(zhihu_id,topics,title,content,answer_num,comments_num,watch_user_num,click_num,crawl_time,url)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE content=VALUES(content),
            answer_num=VALUES(answer_num),comments_num=VALUES(comments_num),watch_user_num=VALUES(watch_user_num),click_num=VALUES(click_num),update_time=VALUES(update_time)
        """
        zhihu_id=self['zhihu_id'][0]
        topics=','.join(self['topics'])
        url=self['url'][0]#''.join(self['url'])
        title=''.join(self['title'])
        content=''.join(self['content'])
        answer_num=extract_nums(''.join(self['answer_num']))
        comments_num=extract_nums(''.join(self['comments_num']))
        watch_user_num=extract_nums(''.join(self['watch_user_num']))
        click_num=extract_nums(''.join(self['click_num']))
        crawl_time=datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)#转换成一种字符串时间
        params=(zhihu_id, topics,title,content,answer_num,comments_num,watch_user_num,click_num, crawl_time,url)
        return insert_sql,params
class ZhihuAnswerItem(scrapy.Item):
    #知乎问题回答item
    zhihu_id=scrapy.Field()
    url=scrapy.Field()
    question_id=scrapy.Field()
    author_id=scrapy.Field()
    content=scrapy.Field()
    parise_num=scrapy.Field()
    comment_num=scrapy.Field()
    create_time=scrapy.Field()
    update_time=scrapy.Field()
    crawl_time=scrapy.Field()
    #mysql特有的ON DUPLICATE KEY UPDATE content=VALUES(content),代表当主键冲突是执行更新操作VALUES(content这个值是从insert当中的content获取)
    def get_insert_sql(self):
        insert_sql="""
            insert into zhihu_answer(zhihu_id,url,question_id,content,praise_num,comments_num,
            create_time,update_time,crawl_time,author_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE content=VALUES(content),
            praise_num=VALUES(praise_num),comments_num=VALUES(comments_num),update_time=VALUES(update_time)
        """
        create_time=datetime.datetime.fromtimestamp(self['create_time']).strftime(SQL_DATETIME_FORMAT)
        update_time=datetime.datetime.fromtimestamp(self['update_time']).strftime(SQL_DATETIME_FORMAT)#将int类型时间转换成date类型，然后再将date类型转换成datetime类型
        params=(self['zhihu_id'],self['url'],self['question_id'],self['content'],self['parise_num']
                ,self['comments_num'],
                create_time,update_time,
                self['crawl_time'].strftime(SQL_DATETIME_FORMAT)
                ,self['author_id'])
        return insert_sql,params
class LagouJobItemLoader(ItemLoader):#重载itemloader类
    #自定义itemloader
    default_output_processor =TakeFirst()#因为示意itemloader所生成的item是以list存储的，所以提取list数组当中的第一个元素进行输出（str）
def remove_splash(value):
    #去掉工作城市的斜杠
    return value.replace('/','')
def handle_jobaddr(value):
    addr_list=value.split('\n')
    addr_list=[item.strip() for item in addr_list if item.strip()!='查看地图']
    return ''.join(addr_list)

class LagouJobItem(scrapy.Item):

    #拉勾网的职位信息
    title=scrapy.Field()
    url=scrapy.Field()
    url_object_id=scrapy.Field()
    salary=scrapy.Field()
    job_city=scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    work_years=scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    degree_need=scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    job_type=scrapy.Field()
    publish_time=scrapy.Field()
    job_advantage=scrapy.Field()
    job_desc=scrapy.Field()
    job_addr=scrapy.Field(
        input_processor=MapCompose(remove_tags,handle_jobaddr)
    )
    company_name=scrapy.Field()
    company_url=scrapy.Field()
    tags=scrapy.Field(
        input_processor=Join(',')
    )
    crawl_time=scrapy.Field()
    crawl_update_time=scrapy.Field()
    def get_insert_sql(self):
        insert_sql="""
           insert into lagou_job(url,url_object_id,
           title,salary,
           job_city,work_years,degree_need
           ,job_type,publish_time,
           tags,job_advantage,job_desc,
           job_addr,company_url,company_name,crawl_time)
           values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
           ON DUPLICATE KEY UPDATE title=VALUES(title),salary=VALUES(salary),
            job_advantage=VALUES(job_advantage),job_desc=VALUES(job_desc),job_addr=VALUES(job_addr)
        """
        params=(self['url'],self['url_object_id'],
                self['title'],self['salary'],
                self['job_city'],self['work_years'],self['degree_need']
                ,self['job_type'],self['publish_time'],self['tags'],self['job_advantage'],self['job_desc'],
           self['job_addr'],self['company_url'],self['company_name'],self['crawl_time'].strftime(SQL_DATETIME_FORMAT))
        return insert_sql,params





