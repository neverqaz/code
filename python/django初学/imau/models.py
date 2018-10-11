# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bookhouse(models.Model):
    house_id = models.AutoField(db_column='House_ID', primary_key=True)  # Field name made lowercase.
    house_name = models.CharField(db_column='House_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BookHouse'
        verbose_name='出版社'
        verbose_name_plural=verbose_name
    def __str__(self):
         return  self.house_name


class Bookinfo(models.Model):
    book_id = models.IntegerField(db_column='Book_ID', primary_key=True)  # Field name made lowercase.
    book_name = models.CharField(db_column='Book_Name', max_length=60)  # Field name made lowercase.
    book_author = models.CharField(db_column='Book_Author', max_length=60)  # Field name made lowercase.
    book_price = models.FloatField(db_column='Book_Price')  # Field name made lowercase.
    book_house = models.CharField(db_column='Book_House', max_length=50)  # Field name made lowercase.
    book_number = models.IntegerField(db_column='Book_Number')  # Field name made lowercase.
    book_type = models.CharField(db_column='Book_Type', max_length=50)  # Field name made lowercase.
    #image=models.ImageField(upload_to='courses/%Y/%m')
    class Meta:
        managed = False
        db_table = 'BookInfo'
    def __str__(self):
        return  self.book_name,self.book_author


class Booktype(models.Model):
    type_id = models.AutoField(db_column='Type_ID', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='Type_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BookType'
    def __str__(self):
        return self.type_name

from django.contrib.auth.models import AbstractUser
class Users1(AbstractUser):
    sex=models.CharField(max_length=20,default='男')
    last_name = None#重写不用
    first_name = None
    class Meta:
        managed=True

class Users(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=50)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
    def __str__(self):
        return self.user_name
import datetime
class Article (models.Model):
    article_id=models.AutoField(primary_key=True ,null=False,blank=False,verbose_name='文章id')#自增字段从1开始增
    body=models.TextField(verbose_name='文章内容')
    author=models.ForeignKey(Users)
    title=models.CharField(max_length=50,null=False)
    type=models.IntegerField(verbose_name='文章类型',default=1)
    create_time=models.DateTimeField(default=datetime.datetime.now())
    class Meta:#源
        managed=True#同步导数据库里
        db_table='article'


