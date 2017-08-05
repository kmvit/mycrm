from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^$', OrderList.as_view(), name='order_list'),
    url(r'^(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^add/$', OrderAdd.as_view(), name='order_add'),
    url(r'^(?P<pk>\d+)/edit$', OrderEdit.as_view(), name='order_edit'),
    url(r'^(?P<pk>\d+)/delete$', OrderDelete.as_view(), name='order_delete'),
    url(r'^send/(?P<order_id>\d+)/$', order_send, name='order_send'),
    url(r'^send/(?P<order_id>\d+)/sms$', order_sms, name='order_sms'),
    url(r'^(?P<order_id>\d+)/master/$', order_master_chenged, name='master_changed'),
    url(r'^filter/$', order_filter, name='order_filter'),
]