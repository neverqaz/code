# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 05:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0025_auto_20181006_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alipayordersettle',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 6, 13, 5, 8, 675499), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 6, 13, 5, 8, 676195), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 6, 13, 5, 8, 676803), verbose_name='添加时间'),
        ),
    ]
