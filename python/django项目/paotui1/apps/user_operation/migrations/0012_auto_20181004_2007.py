# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-04 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0011_auto_20181002_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='district',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='province',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='address_point',
            field=models.CharField(default='', max_length=100, verbose_name='地址坐标'),
        ),
        migrations.AlterField(
            model_name='alipayordersettle',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 20, 7, 12, 618150), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 20, 7, 12, 619169), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 20, 7, 12, 620105), verbose_name='添加时间'),
        ),
    ]
