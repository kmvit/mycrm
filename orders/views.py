from django.shortcuts import render, reverse, HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import orders
from .models import *
from masters.models import Master
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .forms import *


# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Order


@method_decorator(login_required, name='dispatch')
class OrderDetail(DetailView):
    model = Order

@method_decorator(login_required, name='dispatch')
class OrderAdd(CreateView):
    model = Order
    form_class = OrderAddForm

@method_decorator(login_required, name='dispatch')
class OrderSend(ListView):
    model = Master
    template_name = 'orders/send_master.html'


def order_filter(request):
    """Фильтр заказов"""
    if 'select' in request.GET and request.GET['select']=='all':
        order_list = Order.objects.all()
    else:
        order_list = Order.objects.filter(status = request.GET.get('select'))
    context = {'order_list':order_list}
    return render(request, 'orders/order_list.html', context)


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


def order_update(request, form, order_id):
    """Запись мастеров в заказ"""
    order = Order.objects.get(id=order_id)
    order.master_send_sms = form.cleaned_data['']


def sms(request, order_id):
    order = Order.objects.get(id=order_id)
    if 'master' in request.POST:
        order.master_send_sms = request.POST.getlist('master')
        order.save()
        return HttpResponse('ок')
    else:
        return HttpResponse(request.POST.getlist('master'))



from urllib.request import Request, urlopen
from optparse import OptionParser


def sendsms(idsender, subject, to):
    subject = subject.replace(" ", "+")
    url = "http://sms.ru/sms/send?api_id=%s&text=%s&to=%s" % (idsender, subject, to)
    res = urlopen(url)


def change_master(request):
    parser = OptionParser()
    parser.add_option("-i", "--idsender", dest="idsender", default="83F28281-2704-6800-9A35-468003306417",
                      help="ID user on sms.ru", metavar="IDSENDER")
    parser.add_option("-t", "--to", dest="to", default="79289557566", help="to telephone number", metavar="TO")
    parser.add_option("-s", "--subject", dest="subject", default="Hello", help="Name of subject", metavar="SUBJECT")
    (options, args) = parser.parse_args()
    sendsms(options.idsender, options.subject, options.to)