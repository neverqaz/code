from django.db import models
import  datetime
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import AbstractUser
class Article(models.Model):
    aid=models.AutoField(primary_key=True,null=False,blank=False,verbose_name='文章编号')
    title=models.CharField(max_length=100,null=False,verbose_name='文章标题')
    context=UEditorField('内容', height=300, width=798.48, default='', blank=True,
                        imagePath="images/",
                        toolbars='full', filePath='files/')
    slug=models.TextField(verbose_name='文章简述',max_length=1000)
    category=models.CharField(max_length=100,verbose_name='文章类型')
    author=models.CharField(max_length=100,verbose_name='文章作者')
    image=models.ImageField(upload_to='blog/%Y/%m',verbose_name='图片')
    image1=models.ImageField(upload_to='blog/%Y/%m', verbose_name='图片1',default='')
    image2=models.ImageField(upload_to='blog/%Y/%m', verbose_name='图片2',default='')
    image3=models.ImageField(upload_to='blog/%Y/%m', verbose_name='图片3',default='')
    createtime=models.DateTimeField(verbose_name='发布时间')
    class Meta:
        managed=True
        db_table='artile'
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.aid)
    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='/'>跳转</>")

class Comment(models.Model):
    cid = models.AutoField(primary_key=True, null=False, blank=False,verbose_name='评论编号')
    aid=models.ForeignKey('Article',verbose_name='文章编号')
    email=models.CharField(max_length=200,verbose_name='电子邮箱')
    message=models.TextField(verbose_name='评论内容')
    createtime=models.DateTimeField(verbose_name='发布时间')
    class Meta:
        managed=True
        db_table='comment'
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='/'>跳转</>")


class User(AbstractUser):
    first_name=None
    last_name=None
    class Meta:
        managed=True;
        verbose_name='博主设置'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username