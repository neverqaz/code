# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 11:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imau', '0007_auto_20180709_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 9, 19, 16, 11, 591590)),
        ),
    ]
