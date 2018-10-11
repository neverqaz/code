# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 02:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20181005_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 2, 4, 37, 759770, tzinfo=utc), help_text='添加时间', verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_emergency',
            field=models.IntegerField(blank=True, choices=[(2, '着急'), (3, '一般'), (1, '非常着急')], default=3, help_text='(1)非常着急,(2)着急,(3)一般', null=True, verbose_name='订单紧急程度'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(blank=True, choices=[(2, '未完成'), (3, '取消'), (1, '完成'), (4, '创建')], default=4, help_text='(1)完成,(2)未完成,(3)取消,(4)创建', null=True, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.IntegerField(blank=True, choices=[(3, '送东西类'), (2, '快递类'), (1, '带饭类')], default=1, help_text='(1)带饭类,(2)快递类,(3)送东西类', null=True, verbose_name='订单类型'),
        ),
    ]
