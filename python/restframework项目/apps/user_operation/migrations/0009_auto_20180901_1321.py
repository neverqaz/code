# Generated by Django 2.1 on 2018-09-01 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0008_auto_20180901_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 21, 19, 176276), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 21, 19, 172984), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 21, 19, 174776), verbose_name='添加时间'),
        ),
    ]
