# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20170805_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='79289999999', max_length=11, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='order',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Начало работ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Выполнен'), ('2', 'В работе'), ('3', 'Невыполнен'), ('4', 'Отказ')], default=3, max_length=10, verbose_name='Статус'),
        ),
    ]
