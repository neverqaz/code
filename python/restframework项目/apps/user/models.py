from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from datetime import datetime


class UserProfile(AbstractUser):
   """
   用户
   """
   name=models.CharField(max_length=30,null=True,blank=True,verbose_name='姓名')
   birthday=models.DateField(null=True,blank=True,verbose_name='出生年月')
   gender=models.CharField(max_length=6,choices=(("male",u"男"),("female","女")),default='female',verbose_name='性别')
   mobile=models.CharField(null=True,blank=True,max_length=11,verbose_name='电话')
   email = models.CharField(max_length=100,null=True,blank=True,verbose_name='邮箱')


   class Meta:
       verbose_name='用户'
       verbose_name_plural=verbose_name
   def __str__(self):
       return self.username

class VerifyCode(models.Model):
    """
    短信验证码
    """
    code=models.CharField(max_length=10,verbose_name="验证码")
    mobile=models.CharField(max_length=11,verbose_name='电话')
    add_time=models.DateTimeField(default=datetime.now(),verbose_name='添加时间')


    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.code
#信号量设置密码保存不以明码保存
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


User = get_user_model()


@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
            password=instance.password
            instance.set_password(password)
            instance.save()