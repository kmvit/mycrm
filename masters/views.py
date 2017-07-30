from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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