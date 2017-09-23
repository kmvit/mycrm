from django.contrib import admin
from .models import *
# Register your models here.

class MasterAdmin(admin.ModelAdmin):
    list_display = ['id','fio','phone', 'size', 'contract']
    list_filter = ['profession','work', 'city']

admin.site.register(Master, MasterAdmin)


