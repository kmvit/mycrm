# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0002_auto_20170727_1403'),
        ('orders', '0005_auto_20170727_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='master',
            field=models.ManyToManyField(to='masters.Master', verbose_name='Мастера'),
        ),
    ]