# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 09:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20181001_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 1, 17, 22, 0, 855822), help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_emergency',
            field=models.IntegerField(blank=True, choices=[(1, '非常着急'), (3, '一般'), (2, '着急')], default=3, help_text='(1)非常着急,(2)着急,(3)一般', null=True, verbose_name='订单紧急程度'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(blank=True, choices=[(3, '取消'), (2, '未完成'), (1, '完成'), (4, '创建')], default=4, help_text='(1)完成,(2)未完成,(3)取消,(4)创建', null=True, verbose_name='订单状态'),
        ),
    ]
