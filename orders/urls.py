from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', OrderList.as_view(), name='order_list'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^add/$', OrderAdd.as_view(), name='order_add'),
    url(r'^send/(?P<order_id>\d+)/$', order_send, name='order_send'),
    url(r'^send/(?P<order_id>\d+)/sms$', sms, name='order_sms'),
    url(r'^filter/$', order_filter, name='order_filter'),
]