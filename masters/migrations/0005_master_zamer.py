# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0004_auto_20170810_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='zamer',
            field=models.BooleanField(default=False, verbose_name='Замеры'),
        ),
    ]
