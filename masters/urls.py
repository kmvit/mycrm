from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MasterDetail.as_view(), name='master_detail'),
    url(r'^(?P<pk>\d+)/edit$', MasterUpdate.as_view(), name='master_edit'),
    url(r'^(?P<pk>\d+)/delete$', MasterDelete.as_view(), name='master_delete'),
    url(r'^add/$', MasterAdd.as_view(), name='master_add'),
    url(r'^filter/$', master_filter, name='master_filter'),
    url(r'^$', MasterList.as_view(), name='master_list'),
]