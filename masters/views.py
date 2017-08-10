from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *


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
            master_list = Master.objects.filter(work = select)
        else:
            master_list = Master.objects.filter(work = request.GET.get('select'), city__id = request.GET.get('city-select'))
    work_list = Work.objects.all()
    city_list = City.objects.all()
    profession_list = Profession.objects.all()
    context = {'master_list':master_list, 'work_list':work_list, 'profession_list':profession_list , 'city_list':city_list}
    return render(request, 'masters/master_list.html', context)