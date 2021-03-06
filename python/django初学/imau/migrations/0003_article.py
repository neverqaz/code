# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imau', '0002_auto_20180709_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章id')),
                ('body', models.TextField(verbose_name='文章内容')),
                ('title', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imau.Users')),
            ],
            options={
                'managed': True,
                'db_table': 'article',
            },
        ),
    ]
