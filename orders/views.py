from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DeleteView, DetailView
# Create your views here.

class OrderList(ListView):
    model = Order

class OrderDetail(DetailView):
    model = Order