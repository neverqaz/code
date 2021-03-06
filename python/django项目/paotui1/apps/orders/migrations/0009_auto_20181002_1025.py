# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 02:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20181001_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 10, 25, 4, 672401), help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_emergency',
            field=models.IntegerField(blank=True, choices=[(3, '一般'), (2, '着急'), (1, '非常着急')], default=3, help_text='(1)非常着急,(2)着急,(3)一般', null=True, verbose_name='订单紧急程度'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(blank=True, choices=[(2, '未完成'), (1, '完成'), (4, '创建'), (3, '取消')], default=4, help_text='(1)完成,(2)未完成,(3)取消,(4)创建', null=True, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.IntegerField(blank=True, choices=[(1, '带饭类'), (3, '送东西类'), (2, '快递类')], default=1, help_text='(1)带饭类,(2)快递类,(3)送东西类', null=True, verbose_name='订单类型'),
        ),
    ]
