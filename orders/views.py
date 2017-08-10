from django.shortcuts import render, reverse, HttpResponse ,HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import orders
from .models import *
from masters.models import Master
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .forms import *
from urllib.request import Request, urlopen
from urllib.parse import quote
from datetime import datetime

# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Order


@method_decorator(login_required, name='dispatch')
class OrderDetail(DetailView):
    model = Order
    
    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context['master_list'] = Master.objects.filter(id__in=self.object.master_send_sms.all())
        return context

@method_decorator(login_required, name='dispatch')
class OrderAdd(CreateView):
    model = Order
    form_class = OrderAddForm


@method_decorator(login_required, name='dispatch')
class OrderEdit(UpdateView):
    model = Order
    form_class = OrderEditForm
    template_name = 'orders/order_edit.html'
    
    def get_success_url(self):
        return reverse('orders:order_detail', kwargs={'pk': self.object.id})
        
        
@method_decorator(login_required, name='dispatch')
class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:order_list')


@method_decorator(login_required, name='dispatch')
class OrderSend(ListView):
    model = Master
    template_name = 'orders/send_master.html'


@login_required
def order_filter(request):
    """Фильтр заказов"""
    if 'select' in request.GET and request.GET['select']=='all':
        order_list = Order.objects.all()
    else:
        order_list = Order.objects.filter(status = request.GET.get('select'))
    context = {'order_list':order_list}
    return render(request, 'orders/order_list.html', context)

@login_required
def master_filter(request):
    """Фильтр мастеров"""
    if 'select' in request.GET and request.GET['select'] == 'all':
        master_list = Master.objects.all()
    context = {'master_list':master_list}
    return render(request, 'masters/maste_list.html', context)


def order_send(request, order_id):
    """Выбор мастеров после создания заказа"""
    order = Order.objects.get(id = order_id)
    master_list = Master.objects.filter(city__in = order.city.all())
    context = {'master_list':master_list, 'order':order}
    return render (request, 'orders/send_master.html', context)

    
def order_sms(request, order_id):
    """Запись мастеров в заказ"""
    order = Order.objects.get(id=order_id)
    phone_number = []
    for item in order.master_send_sms.all():
        phone_number.append(item.phone)
    message = request.POST['message']
    if 'master' in request.POST:
        order.master_send_sms = request.POST.getlist('master')
        order.save()
        idsender = "83F28281-2704-6800-9A35-468003306417"
        subject = quote(message)
        to = '79289557566'
        
        #return HttpResponse(phone_number)
        url = "http://sms.ru/sms/send?api_id=%s&text=%s&to=%s" % (idsender, subject, to)
        res = urlopen(url)
        return redirect('orders:order_detail', pk = order_id)

    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def order_master_chenged(request, order_id):
    """Запись мастера исполнителя в заказ"""
    order = Order.objects.get(id=order_id)
    if 'master' in request.POST:
        order.master_changed = request.POST.get('master')
        order.start = datetime.now()
        order.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        

@method_decorator(login_required, name='dispatch')
class AddCity(CreateView):
    model = City
    form_class = CityForm
    success_url = reverse_lazy('orders:order_list')

@method_decorator(login_required, name='dispatch')
class AddProffesion(CreateView):
    model = Profession
    form_class = ProffesionForm
    success_url = reverse_lazy('orders:order_list')

@method_decorator(login_required, name='dispatch')
class AddWork(CreateView):
    model = Work
    form_class = WorkForm
    success_url = reverse_lazy('orders:order_list')

