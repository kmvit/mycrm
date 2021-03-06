# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 13:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('born', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата')),
                ('fio', models.CharField(max_length=300, verbose_name='ФИО')),
                ('size', models.IntegerField(max_length=10, verbose_name='Объем')),
                ('description', models.TextField(verbose_name='Примечания')),
                ('contract', models.BooleanField(default=False, verbose_name='Договор')),
                ('city', models.ManyToManyField(to='orders.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Работу',
                'verbose_name_plural': 'Виды работ',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='proffesion',
            field=models.ManyToManyField(to='orders.Profession', verbose_name='Профессия'),
        ),
        migrations.AddField(
            model_name='order',
            name='work',
            field=models.ManyToManyField(to='orders.Work', verbose_name='Виды работ'),
        ),
    ]
