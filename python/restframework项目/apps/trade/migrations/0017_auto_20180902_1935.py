# Generated by Django 2.1 on 2018-09-02 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0016_auto_20180902_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='num',
            new_name='nums',
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 2, 19, 35, 20, 19181), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 2, 19, 35, 20, 18517), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 2, 19, 35, 20, 17751), verbose_name='添加时间'),
        ),
    ]
