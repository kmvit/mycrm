from django.forms import ModelForm, CheckboxSelectMultiple, SelectMultiple
from .models import *


class OrderAddForm(ModelForm):
    class Meta:
        model = Order
        fields='__all__'
        exclude = ['master_send_sms', 'master_changed', 'status']
        widgets = {
            'work': SelectMultiple()
        }


class OrderEditForm(ModelForm):
    class Meta:
        model = Order
        fields='__all__'
        exclude = ['master_send_sms', 'master_changed']
        widgets = {
            'work': SelectMultiple()
        }
        
class CityForm(ModelForm):
    class Meta:
        model = City
        fields='__all__'

class ProffesionForm(ModelForm):
    class Meta:
        model = Profession
        fields='__all__'
        
class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields='__all__'