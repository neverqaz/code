# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 10:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0020_auto_20181005_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alipayordersettle',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 18, 40, 38, 702309), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 18, 40, 38, 703152), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 18, 40, 38, 703966), verbose_name='添加时间'),
        ),
    ]
