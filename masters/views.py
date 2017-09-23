from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from orders.models import Order


@login_required
def home(request):
    return render(request, 'index.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        login(request, user)
        # Перенаправление на "правильную" страницу
        return render(request,'masters/index.html')
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")
        

def logout_view(request):
    logout(request)
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class MasterList(ListView):
    model = Master
    def get_context_data(self, **kwargs):
        context = super(MasterList, self).get_context_data(**kwargs)
        context['work_list'] = Work.objects.all()
        context['profession_list'] = Profession.objects.all()
        context['city_list'] = City.objects.all()
        context['order_finish'] = Order.objects.filter(status = '1')
        return context

@method_decorator(login_required, name='dispatch')
class MasterDetail(DetailView):
    model = Master

@method_decorator(login_required, name='dispatch')
class MasterAdd(CreateView):
    model = Master
    form_class = MasterAddForm
    success_url = '/masters'
    
    def get_context_data(self, **kwargs):
        context = super(MasterAdd, self).get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        context['work_list'] = Work.objects.all()
        context['profession_list'] = Profession.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class MasterUpdate(UpdateView):
    model = Master
    form_class = MasterAddForm
    success_url = '/masters'
    template_name = 'masters/master_edit.html'
    
@method_decorator(login_required, name='dispatch')
class MasterDelete(DeleteView):
    model = Master
    success_url = '/masters'

def master_filter(request):
    """Фильтр мастеров"""
    if 'select' in request.GET and 'city-select' in request.GET:
        select = request.GET['select']
        city = request.GET['city-select']
        if select == "all" and city == "all":
            master_list = Master.objects.all()
        elif select == 'all':
            master_list = Master.objects.filter(city__id = city)
        elif city == 'all':
            master_list = Master.objects.filter(work__in = request.GET.getlist('select'))
        else:
            master_list = Master.objects.filter(work__in = request.GET.getlist('select'), city__id = request.GET.get('city-select'))
    elif 'city-select' in request.GET:
        master_list = Master.objects.filter(city__id = request.GET.get('city-select'))
    elif 'select' in request.GET:
        master_list = Master.objects.filter(work__in = request.GET.get('select'))
    else:
        master_list = Master.objects.all()
    work_list = Work.objects.all()
    city_list = City.objects.all()
    profession_list = Profession.objects.all()
    context = {'work_list':work_list, 'profession_list':profession_list , 'city_list':city_list, 'master_list':master_list, }
    return render(request, 'masters/master_list.html', context)

def change_id(request):
    masters = Master.objects.all()
    i = 1
    for master in masters:
        master.id = i
        i+=1
        master.save()
    return HttpResponse('ok')
