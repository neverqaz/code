# Generated by Django 2.1 on 2018-09-02 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20180902_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 2, 19, 33, 28, 236008), verbose_name='添加时间'),
        ),
    ]
