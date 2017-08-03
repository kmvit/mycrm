from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MasterDetail.as_view(), name='master_detail'),
    url(r'^add/$', MasterAdd.as_view(), name='master_add'),
    url(r'^$', MasterList.as_view(), name='master_list'),
]