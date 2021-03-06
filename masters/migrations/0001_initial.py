# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0005_auto_20170727_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=300, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('contract', models.BooleanField(default=False, verbose_name='Договор')),
                ('size', models.IntegerField(max_length=2, verbose_name='Человек в бригаде')),
                ('city', models.ManyToManyField(to='orders.City', verbose_name='Город')),
                ('proffesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Profession', verbose_name='Профессия')),
                ('work', models.ManyToManyField(to='orders.Work', verbose_name='Виды работ')),
            ],
            options={
                'verbose_name_plural': 'Мастера',
                'verbose_name': 'Мастер',
            },
        ),
    ]
