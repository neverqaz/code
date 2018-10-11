# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#数据存取并且可以拦截我们的item，将数据保存到我们的数库和文件当中以及json当中
from scrapy.pipelines.images import ImagesPipeline
import codecs#打开文件比open的方法好原因在于避免很多编码问题
import json
import MySQLdb
import MySQLdb.cursors
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item
#处理图片下载完成之后路径
class ArticleIamgePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):#（ImagesPipeline类的执行函数，重写）
        if 'front_image_url' in item:
            for ok,value in results:
                image_file_path=value['path']
                item['front_image_path']=image_file_path
        return item
#方法一：自定义json文件的导出，建立到保存到json当中的pipeline
class JsonWithEncodingPipeline(object):
    '''1.在初始化当中打开json文件
    '''
    def __init__(self):
        self.file = codecs.open('article1.json','w',encoding='utf-8')#codecs.open(文件名，读写操作，编码方式)

    def process_item(self, item, spider):#（默认执行函数）
        lines=json.dumps(dict(item),ensure_ascii=False) + "\n"#将item转换为成一个字典再利用json.dumps转换成字符串并且设置编码格式保证中文以及其他编码格式显示正常
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()#爬虫关闭时关闭文件
#方法二：利用scrapy本身提供的写入json文件的机制
class JsonExporterPipeline(object):
    #调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file=open('articleexport.json','wb')#open（文件名，以二进制文件打开方式）
        self.exporter=JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        self.exporter.start_exporting()
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
#方法三保存到数据库爬取的速度要比插入数据库中的速度要快的多，并且插入数据库里面执行的语句是同步执行，不执行完下一条的插入不能进行所以该方法不适用所以利用方法四进行插入数据库
class MysqlPipeline(object):
    #采用同步机制写入数据库
    def __init__(self):
        host='127.0.0.1'
        user='root'
        password='123456'
        dbname='article'
        self.conn=MySQLdb.connect(host,user,password,dbname,charset='utf8',use_unicode=True)
        self.cursor=self.conn.cursor()

    def process_item(self, item, spider):
        '''  title=scrapy.Field()
    post_time=scrapy.Field()
    url=scrapy.Field()
    url_object_id=scrapy.Field()#使我们的url变为长度固定的唯一值
    front_image_url=scrapy.Field()
    front_image_path=scrapy.Field()
    praise_nums=scrapy.Field()
    comment_nums=scrapy.Field()
    fav_nums=scrapy.Field()
    tags=scrapy.Field()
    content'''
        insert_sql="""
        insert into article(title,post_time,url,url_object_id,front_image_url,front_image_path,praise_nums,comment_nums,fav_nums,tags,content)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(insert_sql,(item['title'],item['post_time'],item['url'],item['url_object_id'],item['front_image_url'],item['front_image_path'],item['praise_nums'],item['comment_nums'],item['fav_nums'],item['tags'],item['content']))
        self.conn.autocommit()
        return item
#方法四利用twised的连接池进行数据库 和爬虫的异步操作
class MysqlTwsiedPipeline(object):
    def __init__(self,dbpool1):#利用初始化函数来接收刚才实例化的dbpool
        self.dbpool=dbpool1
    @classmethod#自定义自己的组件会被scrapy初始化时调用,在 settings定义了数据库的连接字段通过该方法调用setttings.py文件中的数据库字段
    def from_settings(cls,settings):#cls 代表本身自己类（MysqlTwsiedPipeline）
       dbparms= dict(#该字典的属性名要和mysqlconnect函数的变量名保持一制
        host=settings['MYSQL_HOST'],
        db=settings['MYSQL_DBNAME'],
        user=settings['MYSQL_USER'],
        passwd=settings['MYSQL_PASSWORD'],
        charset='utf8',
        cursorclass=MySQLdb.cursors.DictCursor,
        use_unicode=True,
        )
       dbpool=adbapi.ConnectionPool("MySQLdb",**dbparms)
       return cls(dbpool)#我们需要调用这个类并且实例化对象（实例化这MysqlTwsiedPipeline类）

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query=self.dbpool.runInteraction(self.do_insert,item)#（具体执行的动作，item）
        query.addErrback(self.handle_error,item,spider)#添加异步处理错误函数，因为不是同步的所以不会及时返回错误信息
        return item
    def handle_error(self,failure,item,spider):
        #处理异步插入的异常
        print(failure)
    def do_insert(self,cursor,item):
        #执行具体的插入

       # if item.__class___.__name__=='ArticleItem':#该用法可以去到当前item中类的名字
#             insert_sql = """insert into article(title,post_time,url,url_object_id,
# front_image_url,front_image_path,praise_nums,comment_nums,fav_nums,tags,content)
# VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#                 """
#             cursor.execute(insert_sql,(item['title'],item['post_time'],item['url'],item['url_object_id'],item['front_image_url']
#                                    ,item['front_image_path'],item['praise_nums'],
#                                    item['comment_nums'],item['fav_nums'],item['tags'],item['content']))


# 根据不同的item 构建不同的sql语句并插入到mysql中
          insertsql,params=item.get_insert_sql()
          cursor.execute(insertsql,params)