from django.contrib import admin
from .models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','born','status']
    list_filter = ['status','city']

admin.site.register(City)
admin.site.register(Profession)
admin.site.register(Work)
admin.site.register(Order, OrderAdmin)