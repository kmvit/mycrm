# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20170810_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='contract',
        ),
    ]