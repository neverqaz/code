# Generated by Django 2.1 on 2018-08-31 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180831_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 13, 10, 16, 103084), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 13, 10, 16, 98807), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 13, 10, 16, 96601), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 13, 10, 16, 97666), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 13, 10, 16, 99807), verbose_name='添加时间'),
        ),
    ]
