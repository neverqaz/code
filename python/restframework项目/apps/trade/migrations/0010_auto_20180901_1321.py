# Generated by Django 2.1 on 2018-09-01 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0009_auto_20180901_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 21, 19, 170753), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 21, 19, 169252), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 21, 19, 167527), verbose_name='添加时间'),
        ),
    ]
