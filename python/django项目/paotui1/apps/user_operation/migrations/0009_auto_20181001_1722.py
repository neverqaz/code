# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 09:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0008_auto_20181001_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='alipayordersettle',
            name='out_trade_no',
            field=models.CharField(blank=True, help_text='商户订单号', max_length=50, null=True, verbose_name='商户订单号'),
        ),
        migrations.AlterField(
            model_name='alipayordersettle',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 1, 17, 22, 0, 851868), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='alipayordersettle',
            name='out_request_no',
            field=models.CharField(blank=True, help_text='结算流水号', max_length=50, null=True, verbose_name='结算流水号'),
        ),
        migrations.AlterField(
            model_name='alipayordersettle',
            name='trans_in',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='收入方用户号'),
        ),
        migrations.AlterField(
            model_name='alipayordersettle',
            name='trans_out',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='支出方用户号'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 1, 17, 22, 0, 852652), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 1, 17, 22, 0, 853286), verbose_name='添加时间'),
        ),
    ]
