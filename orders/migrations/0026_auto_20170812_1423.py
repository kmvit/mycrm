# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_remove_order_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Начало работ'),
        ),
    ]
