# Generated by Django 2.1 on 2018-09-01 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20180831_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 11, 5, 45, 833070), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 11, 5, 45, 831396), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 11, 5, 45, 829927), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 11, 5, 45, 830580), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 11, 5, 45, 832409), verbose_name='添加时间'),
        ),
    ]
