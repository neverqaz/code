from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime
# Create your models here.
User=get_user_model()
class UserFav(models.Model):
    """
    用户收藏
    """
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together=("goods","user")#收藏记录不在重复

    def __str__(self):
        return self.user.username
class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES=(
        (1,"留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购"),

    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    msg_type=models.IntegerField(default=1,choices=MESSAGE_CHOICES,verbose_name="消息类型",
                                 help_text=u"留言类型：(1)留言,(2)投诉,(3)询问,(4)售后,(5)求购")
    subject=models.CharField(max_length=100,default="",verbose_name="主题")
    message=models.TextField(default="",verbose_name="留言内容",help_text="留言内容")
    file=models.FileField(verbose_name="上传文件",help_text="上传文件",upload_to="message/",default="")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    province= models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address = models.CharField(max_length=100, default="", verbose_name="详细地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='添加时间')

    class Meta:
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver






@receiver(post_save, sender=UserFav)
def create_userfav(sender, instance=None, created=False, **kwargs):
    if created:
            goods=instance.goods
            goods.fav_num+=1
            goods.save()

@receiver(post_delete, sender=UserFav)
def delete_userfav(sender, instance=None, created=False, **kwargs):
    if created:
            goods=instance.goods
            goods.fav_num-=1
            goods.save()
