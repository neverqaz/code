from django.db import models

#Create your models here.
from django.db import models

from apps.userprofile.models import Users
from datetime import datetime
#from django.utils import timezone as datetime
#Create your models here.
class AlipayOrderSettle(models.Model):
    """支付宝结算"""
    useraos=models.ForeignKey(Users,verbose_name="结算用户")
    #商户自己生成的订单号
    out_trade_no=models.CharField(max_length=50,null=True,blank=True,verbose_name="商户订单号",help_text="商户订单号")
    #发单用户结算完成之后所生成的支付宝交易号
    alipay_trade_no=models.CharField(max_length=50,null=True,blank=True,verbose_name="支付宝交易号",help_text="支付宝交易号")
    order_id=models.IntegerField(blank=True,null=True,verbose_name="订单id")
    #商户自己生成的结算号
    out_request_no=models.CharField(max_length=50,null=True,blank=True,verbose_name="结算流水号",help_text="结算流水号")
    trans_out=models.CharField(max_length=20,null=True,blank=True,verbose_name="支出方用户号")
    trans_in=models.CharField(max_length=20,null=True,blank=True,verbose_name="收入方用户号")
    amount=models.FloatField(default=0,verbose_name="支付金额",help_text="支付金额")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
    class Meta:
        verbose_name="支付宝结算"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.useraos.name if self.useraos.name is not None else self.useraos.username
class UserAddress(models.Model):
    useraddr=models.ForeignKey(Users,verbose_name="用户")
    address_point= models.CharField(max_length=100, default="", verbose_name="地址坐标")
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    user_name = models.CharField(max_length=20, default="", verbose_name="姓名")
    user_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    city=models.CharField(max_length=40, default="", verbose_name="所在城市")
    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
    class Meta:
        verbose_name="用户地址"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.address# if self.useraddr.name is not None else self.useraddr.username
class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES=(
        (1,"留言"),
        (2, "投诉"),
        (3, "询问"),

    )
    userlm = models.ForeignKey(Users,verbose_name="用户")
    msg_type=models.IntegerField(default=1,choices=MESSAGE_CHOICES,verbose_name="消息类型",
                                 help_text=u"留言类型：(1)留言,(2)投诉,(3)询问")
    subject=models.CharField(max_length=100,default="",verbose_name="主题")
    message=models.TextField(default="",verbose_name="留言内容",help_text="留言内容")
    file=models.FileField(verbose_name="上传文件",help_text="上传文件",upload_to="message/",default="")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
class UserAli(models.Model):
    usera = models.ForeignKey(Users, verbose_name="用户")
    nick_name = models.CharField(max_length=30, verbose_name="支付宝昵称", help_text="支付宝昵称", null=True, blank=True)
    avatar = models.CharField(max_length=300, null=True, blank=True, verbose_name="用户头像地址", help_text="用户头像地址")
    userali_id = models.CharField(max_length=50, verbose_name="支付宝id", help_text="支付宝id", blank=True,
                               null=True)

    class Meta:
        verbose_name = '用户支付宝'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.usera.name if self.usera.name is not None else self.usera.username

