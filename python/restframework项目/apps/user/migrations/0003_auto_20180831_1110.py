# Generated by Django 2.1 on 2018-08-31 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180829_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 31, 11, 10, 44, 368580), verbose_name='添加时间'),
        ),
    ]
