# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Users(AbstractUser):
    name=models.CharField(max_length=30,verbose_name='用户姓名',help_text="用户姓名",null=True,blank=True)
    email = models.CharField(max_length=100,verbose_name="电子邮件",help_text="电子邮件",null=True,blank=True)
    birthday=models.DateField(null=True,blank=True,verbose_name="出生日期",help_text="出生日期")
    compus_card=models.CharField(max_length=20,null=True,blank=True,verbose_name="校园卡号",help_text="校园卡号")
    gender=models.CharField(max_length=6,choices=(("male","男"),("female","女")),verbose_name="性别",help_text="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name='电话',help_text='电话')
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name if self.name is not None else  self.username
@receiver(post_save, sender=Users)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
            password=instance.password
            instance.set_password(password)
            instance.save()