# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 11:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20180712_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='createtime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 12, 19, 36, 12, 274378)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createtime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 12, 19, 36, 12, 275355)),
        ),
    ]
