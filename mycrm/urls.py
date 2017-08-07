"""mycrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from masters.views import *
from orders.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^orders/', include('orders.urls', namespace='orders', app_name='orders')),
    url(r'^masters/', include('masters.urls', namespace='masters', app_name='masters')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^cityadd$', AddCity.as_view(), name='add_city'),
    url(r'^proffesionadd$', AddProffesion.as_view(), name='add_proffesion'),
    url(r'^workadd$', AddWork.as_view(), name='add_work'),
    url(r'^logout$', logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)