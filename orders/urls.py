from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', OrderList.as_view(), name='order_list'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
]