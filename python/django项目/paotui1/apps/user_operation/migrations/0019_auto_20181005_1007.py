# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 10:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0018_auto_20181005_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alipayordersettle',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 10, 7, 23, 176440), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 10, 7, 23, 177374), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 10, 7, 23, 178151), verbose_name='添加时间'),
        ),
    ]
