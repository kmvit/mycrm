from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
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

@method_decorator(login_required, name='dispatch')
class MasterList(ListView):
    model = Master
    def get_context_data(self, **kwargs):
        context = super(MasterList, self).get_context_data(**kwargs)
        context['work_list'] = Work.objects.all()
        context['profession_list'] = Profession.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class MasterDetail(DetailView):
    model = Master

@method_decorator(login_required, name='dispatch')
class MasterAdd(CreateView):
    model = Master
    form_class = MasterAddForm
    success_url = '/masters'