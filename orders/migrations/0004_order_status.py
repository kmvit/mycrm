# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20170727_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Выполнен'), ('2', 'Невыполнен')], default=2, max_length=10),
        ),
    ]
