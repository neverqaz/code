# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import json
import re
import datetime
from scrapy.loader import ItemLoader
from ArticleSpider.items import ZhihuAnswerItem,ZhihuQuestionItem
# from ArticleSpider.settings import MY_USER_AGENT
class GithubSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/question/277214294/']
    start_answer_url='https://www.zhihu.com/api/v4/answers/{0}/concerned_upvoters?limit={1}&offset={2}'


    header = {

        'HOST': 'www.zhihu.com',
        'USER-Agent':'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/58.0'

    }
    custom_settings={
        'COOKIES_ENABLED' : True#配置自己的settings文件
    }

    def parse(self, response):
        '''提取出html页面中的所有url，并跟踪这些url进一步爬取
         如果提取的url中格式为/question/xxxxx 就下载之后直接进入解析函数
        '''
        all_urls=response.css('div.Card-section.SimilarQuestions-list meta::attr(content)').extract()
        all_urls=[parse.urljoin(response.url,url) for url in all_urls]
        all_urls=filter(lambda x:True if x.startwith('https') else False,all_urls)#拉码达函数的意思是x代表所有的urls，如果x开头是以https开头则返回true并且赋值all_urls ,否则过滤掉
        for url in all_urls:
            match_obj=re.match('(.*zhihu.com/question/(\d+))(/|$).*',url)
            if match_obj:
                request_url=match_obj.group(1)
                questions_id=match_obj.group(2)
                #如果是/question/相关页面则下载后交由提取函数进行提取
                # import random
                # random_index = random.random(0, len(MY_USER_AGENT) - 1)
                # random_agent = MY_USER_AGENT[random_index]
                # self.header['USER-Agent']=random_agent
                yield scrapy.Request(request_url,headers=self.header,meta={'question_id':questions_id},callback=self.parse_question)
            else:
                yield scrapy.Request(url,headers=self.header,callback=self.parse)
    def parse_question(self,response):
        #处理question页面，从页面中提取具体的queston item
        question_id=int(response.meta.get('question_id', ''))
        item_loader=ItemLoader(item=ZhihuQuestionItem(),response=response)
        item_loader.add_css('title','h1.QuestionHeader-title::text')
        item_loader.add_css('content''div.QuestionHeader-detail')
        item_loader.add_value('url',response.url)
        item_loader.add_css('answer_num','h4.List-headerText span::text')
        item_loader.add_css('comment_num','.QuestionHeader-Comment button::text')
        item_loader.add_value('question_id',question_id)
        item_loader.add_css('watch_user_num''."NumberBoard-itemValue::text')
        item_loader.add_css('topics','.QuestionHeader-topics .Popover div::text')
        question_item=item_loader.load_item()
        yield scrapy.Request(self.start_answer_url.format(question_id,5,0),headers=self.header,callback=self.parse_answer)
        yield question_item

    def parse_answer(self,response):
        #处理question的answer
        ans_json=json.loads(response.text)
        is_end=ans_json['paging']['is_end']
        totals_answer=ans_json['paging']['totals']
        next_url=ans_json['paging']['next']
        #提取question_answer当中的字段
        for answer1 in ans_json['data']:
            answer_item=ZhihuAnswerItem()
            answer_item['zhihu_id']=answer1['id']
            answer_item['url'] = answer1['url']
            answer_item['question_id'] = answer1['question']['id']
            answer_item['author_id'] = answer1['author']['id'] if 'id' in answer1['author'] else None
            answer_item['content']=answer1['content'] if 'content' in answer1 else None
            answer_item['parise_num'] = answer1['voteup_count']
            answer_item['comment_num'] = answer1['comment_count']
            answer_item['create_time'] = answer1['created_time']
            answer_item['update_time'] = answer1['updated_time']
            answer_item['acrawl_time'] =datetime.datetime.now()
            yield answer_item
        if not is_end:
            yield scrapy.Request(next_url, headers=self.header, callback=self.parse_answer)











    def start_requests(self):
        return [scrapy.Request('https://github.com/login',headers=self.header,callback=self.login)]
    def login(self,response):
        response_text=response.text
        result = re.match('.*name="authenticity_token" value="(.*?)"', response.text,re.DOTALL)#正则表达式默认只匹配第一行的数据所以要加参数re.DOTALL
        authenticity_token=''
        if result:

            authenticity_token =(result.group(1))
        if authenticity_token:
            #post_url = 'https://github.com/session'
            post_data = {
                'authenticity_token': authenticity_token,
                'commit': 'Sign in',
                'login': 'neverqaz',
                'password':'1532105342qaz',
                'utf8': '&#x2713;',
                'captcha':''

            }
            import time
            t = str(int(time.time() * 1000))
            captcha_url = 'https://www.zhihu.com/captcha.gif?r={0}&type=login'.format(t)
            yield scrapy.Request(captcha_url,headers=self.header,meta={'post_data':post_data},callback=self.login_after_captcha())#scrapy都是异步的所以在使用回调函数时保证request当中cookie值是同一个值也将意味着session也是同一个，延迟登录
    def login_after_captcha(self,response):
        #验证码之后再来登录

        with open('captcha.jpg', 'wb')as f:
            f.write(response.body)
            f.close()
            # 打开图片
        from PIL import Image
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            pass
        captcha = input('输入验证码\n>')
        post_url = 'https://github.com/session'
        post_data=response.meta.get('post_data',{})
        post_data['captcha']=captcha



        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.header,
            callback=self.check_login
        )]#这里才是登录
    def check_login(self,response):
        #验证服务器的返回数据判断是否成功
        for url in self.start_urls:
            yield scrapy.Request(url,dont_filter=True,headers=self.header)#没有写回调函数默认跳转到parse函数处理



