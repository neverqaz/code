# 大学四年中写过的所有代码，回顾四年当中所有的心路历程。
* 记得第一次接触编程时，当时只是因为一时好奇，大一的生活，课程很少，一个礼拜只有几节课，而我当时并不在计算机院，而是生科院，一个学生物的学生，但是并不喜欢这个专业，无意中生工班的学生开c语言的课，而我们没有开，我就去周末去蹭课，第一次接触感觉好神奇，敲一点命令和语言就可以让电脑可以运行窗口显示出运行结果。结果，这一蹭课就是一个学期，跟着交作业，但是不用考试，当时很开心。C语言是本人接触的第一门编程语言。当时感觉编程很神奇!
.<div align=center><img width="280" height="350" src="https://raw.githubusercontent.com/neverqaz/code/master/%E5%9B%BE%E7%89%87.png"></div>
* 大二刚好有机会因成绩优异可以转专业，于是就去了计算机学院软件工程专业，记得当时理科往工科转是很痛苦的，要补修大一的课程，一个学期要补修四门课，课程从白天排到晚上都是课，每天都是这样过来的，虽然很苦，但是很开心，每天也不用胡思乱想，上课就是上课。但是也很充实，因为那时我的c++和java同时开课，刚开始有些痛苦，每天都要敲代码去实现老师上课讲的东西。因为只有这样才能是你自己学会了，也因为自己敲的时候会遇到一些问题，解决问题的同时也加深了你对这个知识点的巩固，不会的就去问老师，但是老师说：”我虽然是教这个的，但是也不是所有的问题都能解决，我只是个引导者，遇到问题还得你自己解决！“正所谓，师傅领进门，修行在个人。问题只能自己解决。就这样忙忙碌碌的过了一年，我真的很喜欢编程，也是这个原因让我坚持走过了这一年。
* 大三，学校来了一位美籍华人给我们教php，上了一个礼拜的课，写了一个类似博客的东西，把一切php在项目中运用的知识都讲了一遍，后来用独立用php做的校园二手市场项目，再然后在学习课上知识的同时,在自学python语法，django框架，django-restframework，scrapy爬虫框架，写过绝地求生吃鸡主题的博客用django实现的，跟着视频学习，学的动手敲的暮雪生鲜项目django-restframework+vue利用python脚本对支付宝接口的使用以及短信的使用。还跟着视频学了scrapy的爬取知乎等知名网站，以及反爬虫策略，以及框架源码的解读。官方文档的解读。
* 大四开始着手做毕业设计，我们的老师很负责任的告诉我们：“毕业设计做不完别想着走人”。我最后定的题目是校园跑腿网，老师说的这个做成小程序好，我打算走python web，结果我就想了个折中的办法就是做成前后端分离形式的网站，后端用django-restframework 写restful api接口，而前端用vue.js做，这样的话，前台可以很多种选择Android，微信小程序，web端。
* 校园跑腿网的功能：
* （核心功能）
1. 订单（orders）：
    * 订单发布功能
    * 订单列表功能
    * 订单列表详情功能
    * 订单接单功能
     （接单成功后利用百度地图接口生成定位会显示两者直接的距离map）
    * 订单分类功能（按紧急程度分类）
    * 订单评论功能
2. 用户个人中心：
    * 用户信息管理
    * 用户信息的展示
    * 用户信息的修改
    * 支付宝对应用户信息的展示
    * 用户订单管理功能
    * 订单的信息
    * 订单的状态
    * 用户地址管理功能
    * 地址的增删改查(根据百度地图选取自己的位置)
    * 用户评论管理
* （拓展功能，收费项）
    * 聊天功能
* 流程图：
.<div align=center><img width="80%" height="600" src="https://raw.githubusercontent.com/neverqaz/code/master/%E5%9B%BE%E7%89%872.png"></div>
* 接口的使用
1. 短信服务接口："https://api.miaodiyun.com/20150822/affMarkSMS/sendSMS"
2. 订单支付流程：
    * 订单支付接口：https://docs.open.alipay.com/api_1/alipay.trade.page.pay/
    * 订单结算接口：https://docs.open.alipay.com/api_1/alipay.trade.order.settle/
    * 订单退款接口：https://docs.open.alipay.com/api_1/alipay.trade.refund/
    
3. 百度地图接口：
    * 百度地图利用js写的根据输入后点击或者直接点击获取该点的位置信息和经纬度坐标：http://neverqaz.cn/baidu/
    * 算路线距离接口：http://api.map.baidu.com/direction/v1?mode=riding&origin=人大&destination=北京大学&region=北京&output=json&ak=您的AK
    * 定位加导航起调地图接口：
http://api.map.baidu.com/direction?origin=latlng:34.264642646862,108.95108518068|name:我家&destination=大雁塔&mode=driving&region=西安&output=html&src=webapp.baidu.openAPIdemo
.<div align=center><img width="100%" height="350" src="https://raw.githubusercontent.com/neverqaz/code/master/%E8%B7%AF%E5%BE%84%E5%AF%BC%E8%88%AA%E5%9B%BE.png"></div>

    * 根据经纬度坐标由丰泰餐厅到内蒙古农业大学c座 调起百度地图的加密链接：
http://api.map.baidu.com/direction?origin=40.812727%2C111.723332&destination=40.812365%2C111.721962&mode=walking&region=%E5%91%BC%E5%92%8C%E6%B5%A9%E7%89%B9%E5%B8%82&output=html&src=webapp.baidu.openAPIdemo
    * 以及路线距离测算的链接：
http://api.map.baidu.com/direction/v1?mode=walking&origin=40.812727%2C111.723332&destination=40.812365%2C111.721962&output=json&region=%E5%91%BC%E5%92%8C%E6%B5%A9%E7%89%B9%E5%B8%82&ak=unrcs1AVyGvK5Y085KID6mBmkrK62Dmw
* 利用原型迭代工具画的界面：
.<div align=center><img width="60%" height="450" src="https://raw.githubusercontent.com/neverqaz/code/master/%E7%95%8C%E9%9D%A21.png"></div>







