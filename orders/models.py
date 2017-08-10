# -*- coding: utf-8 -*-
from django.shortcuts import reverse
from django.db import models
from datetime import datetime

# Create your models here.

class City(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    class Meta:
        verbose_name='Город'
        verbose_name_plural=' Города'
    
    def __str__(self):
        return self.title

class Profession(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    class Meta:
        verbose_name='Профессия'
        verbose_name_plural='   Профессии'
    
    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    proffesion = models.ForeignKey(Profession, verbose_name='Профессия')
    class Meta:
        verbose_name='Работу'
        verbose_name_plural='  Виды работ'
    
    def __str__(self):
        return self.title

from masters.models import Master

class Order(models.Model):
    born = models.DateTimeField(default=datetime.now, verbose_name='Дата')
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    phone = models.CharField(max_length=11, default='79289999999', verbose_name='Телефон')
    city = models.ManyToManyField(City, verbose_name='Город')
    work = models.ManyToManyField(Work, verbose_name='Виды работ')
    size = models.IntegerField(verbose_name='Объем')
    start = models.DateTimeField(blank=True, verbose_name='Начало работ')
    description = models.TextField(verbose_name='Примечания')
    master_send_sms = models.ManyToManyField(Master, blank=True, verbose_name='Кому отправить СМС')
    master_changed = models.IntegerField(blank=True,null=True, verbose_name='Мастер исполнитель')
    CHOICES = (
    (u'1', u'Выполнен'),
    (u'2', u'В работе'),
    (u'3', u'Невыполнен'),
    (u'4', u'Отказ'),
    )
    status = models.CharField(max_length=10, choices=CHOICES, verbose_name='Статус')
    enter = models.CharField(max_length=300, verbose_name="Вход")

    
    class Meta:
        verbose_name='Заказ'
        verbose_name_plural='    Заказы'

    def get_absolute_url(self):
        return reverse('orders:order_send', kwargs={'order_id': self.id})