# Generated by Django 2.1 on 2018-09-01 15:26

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20180901_1526'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0009_auto_20180901_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 15, 26, 2, 755754), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 15, 26, 2, 754405), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 15, 26, 2, 755131), verbose_name='添加时间'),
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('goods', 'user')},
        ),
    ]
