# -*- coding: utf-8 -*-
from django.db import models
from orders.models import City, Work, Profession
# Create your models here.

class Master(models.Model):
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    city = models.ManyToManyField(City, verbose_name='Город')
    profession = models.ManyToManyField(Profession, verbose_name='Профессия')
    work = models.ManyToManyField(Work, verbose_name='Виды работ')
    contract = models.BooleanField(default=False, verbose_name='Договор')
    zamer = models.BooleanField(default=False, verbose_name='Замеры')
    size = models.IntegerField(verbose_name='Человек в бригаде')
    description = models.TextField(verbose_name='Примечание', blank= True)
    class Meta:
        verbose_name='Мастер'
        verbose_name_plural='Мастера'
    
    def __str__(self):
        return self.fio
