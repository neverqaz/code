# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imau', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.IntegerField(default=1, verbose_name='文章类型'),
        ),
    ]
