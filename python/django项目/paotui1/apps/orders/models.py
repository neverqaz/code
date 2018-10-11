from django.db import models
from datetime import datetime
#from django.utils import timezone as datetime
from apps.userprofile.models import Users
from apps.user_operation.models import UserAddress
"""订单的总金额=第三方购买费+跑腿费+手续费"""
# Create your models here.
"""
order表
订单名，订单类型，下单时间，订单的描述，订单的紧急程度
用户id，订单的总金额，手续费，
跑腿费，第三方购买费用，订单的状态（finsh，unfinish，cancel），
（is_accept=false）
订单的支付状态"""
class Order(models.Model):
    ordertype={
        (1,"带饭类"),
        (2,"快递类"),
        (3,"送东西类")
    }
    emergency={(1,"非常着急"),(2,"着急"),(3,"一般")}
    orderstatus={(1,"完成"),(2,"未完成"),(3,"取消"),(4,'创建')}
    order_pay=(
        ("TRADE_FINISHED","交易完成"),
        ("TRADE_SUCCESS", "支付成功"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_CLOSED", "交易关闭")
        )
    currentuser=models.ForeignKey(Users,verbose_name="用户",help_text="用户",blank=True,null=True,related_query_name="%(app_label)s_%(class)s_user",related_name="%(app_label)s_%(class)s_user")
    currentaddress=models.ForeignKey(UserAddress,verbose_name="下单地址",help_text="下单地址",blank=True,null=True)
    name=models.CharField(max_length=30,null=True,blank=True,verbose_name="订单名称",help_text="订单名称")
    order_sn=models.CharField(max_length=50,null=True,blank=True,verbose_name="订单编号",help_text="订单编号")
    order_type=models.IntegerField(choices=ordertype,
                                   verbose_name="订单类型",help_text="(1)带饭类,(2)快递类,(3)送东西类",null=True,blank=True,default=1)
    order_emergency=models.IntegerField(choices=emergency,verbose_name="订单紧急程度",
                                        help_text="(1)非常着急,(2)着急,(3)一般",null=True,blank=True,default=3)
    order_decs=models.TextField(default="",verbose_name="备注",help_text="备注")
    order_total=models.FloatField(default=0,verbose_name="订单总金额",help_text="订单总金额")
    purchase=models.FloatField(default=0,verbose_name="第三方购买费",help_text="第三方购买费")
    tax=models.FloatField(default=0,verbose_name="手续费",help_text="手续费")
    run_money=models.FloatField(default=0,verbose_name="跑腿费",help_text="跑腿费")
    order_status=models.IntegerField(choices=orderstatus,verbose_name="订单状态",
                                     help_text="(1)完成,(2)未完成,(3)取消,(4)创建",null=True,blank=True,default=4)
    order_pay_status=models.CharField(max_length=30,choices=order_pay,verbose_name="订单支付状态",help_text="订单支付状态",default="WAIT_BUYER_PAY")
    is_accept=models.BooleanField(default=False,verbose_name="是否已接单",help_text="是否已接单")
    distance=models.FloatField(default=0,verbose_name="路程",help_text="路程")
    add_time=models.DateTimeField(default=datetime.now(),verbose_name="添加时间",help_text="添加时间")
    #下单人信息:
    send_user_id=models.IntegerField(blank=True,null=True,verbose_name="下单人id",help_text="下单人id")
    send_address = models.CharField(max_length=100, default="",blank=True,null=True,verbose_name="下单地址",help_text="下单人地址")
    send_name = models.CharField(max_length=20, default="",blank=True,null=True, verbose_name="下单人姓名",help_text="下单人姓名")
    send_mobile = models.CharField(max_length=11, blank=True,null=True,verbose_name="下单人联系电话",help_text="下单人联系电话")
    #接单人信息：
    accept_user_id = models.IntegerField(blank=True, null=True, verbose_name="接单人id",help_text="接单人id")
    accept_address = models.CharField(max_length=100, default="",blank=True,null=True,verbose_name="接单地址",help_text="接单人地址")
    accept_name = models.CharField(max_length=20, default="",blank=True,null=True,verbose_name="接单人姓名",help_text="接单人姓名")
    accept_mobile = models.CharField(max_length=11,blank=True,null=True,verbose_name="接单人联系电话",help_text="接单人联系电话")
    pay_time=models.DateTimeField(blank=True,null=True,verbose_name="支付时间",help_text="支付时间")
    add_time=models.DateTimeField(default=datetime.now(),verbose_name="添加时间",help_text="添加时间")
    class Meta:
        verbose_name="订单"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
"""category表
订单分类：（1）根据订单重要性
（2）订单的着急程度
（3）订单的路程距离
（4）订单的状态
（5）订单的类型：打饭
手续费也根据这些算出
"""
"""user_opration
userpay表
userprofile，
order，
alipay_url,
return_url,

"""
class OrderAccept(models.Model):
    #select_tools=(("walking","步行"),("transit","公交"),("driving","驾车"))
    useroac=models.ForeignKey(Users,verbose_name="接单人",help_text="接单人")
    orderac=models.ForeignKey(Order,verbose_name="订单",help_text="订单")
    addressac=models.ForeignKey(UserAddress,verbose_name="地址信息",help_text="地址信息")
    #tools=models.CharField(choices=select_tools,default="walking",max_length=20,blank=True,null=True,verbose_name="出行方式",help_text='出行方式')
    class Meta:
        verbose_name = '接订单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.useroac.name if self.useroac.name is not None else self.useroac.username






