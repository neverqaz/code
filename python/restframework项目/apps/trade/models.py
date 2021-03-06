from django.db import models
from user.models import UserProfile
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime
# Create your models here.
User=get_user_model()
class ShoppingCart(models.Model):
    """
    购物车
    """
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=u"用户")
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name=u"商品")
    nums=models.IntegerField(default=0,verbose_name="购买数量")
    add_time=models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together=('user','goods')

    def __str__(self):
        return "%s(%d)".format(self.goods.name,self.nums)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS=(
        ("TRADE_FINISHED","交易完成"),
        ("TRADE_SUCCESS", "支付成功"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_CLOSED", "交易关闭")
        )

    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=u"用户")
    order_sn=models.CharField(max_length=30,null=True,blank=True,unique=True,verbose_name="订单号")
    trade_no=models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name="订单编号")
    pay_status=models.CharField(choices=ORDER_STATUS,max_length=30,verbose_name="订单状态",default='paying')
    post_script=models.CharField(max_length=11,verbose_name="订单留言")
    order_mount=models.FloatField(default=0.0,verbose_name="订单金额")
    pay_time=models.DateTimeField(null=True,blank=True,verbose_name="支付时间")

    #用户信息
    address=models.CharField(max_length=100,default="",verbose_name="收货地址")
    signer_name=models.CharField(max_length=20,default="",verbose_name="签收人")
    signer_mobile=models.CharField(max_length=11,verbose_name="联系电话")

    add_time=models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = u'订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)

class OrderGoods(models.Model):
    """
    订单的商品详情
    """
    order=models.ForeignKey(OrderInfo,on_delete=models.CASCADE,verbose_name="订单信息",related_name="goods")
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品")
    goods_num=models.IntegerField(default=0,verbose_name="商品数量")
    add_time=models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = u'订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)

