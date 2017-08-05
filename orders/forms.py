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

    def __init__(self, *args, **kwargs):
        super(OrderAddForm, self).__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
        self.fields['contract'].widget.attrs.update({'class': 'myfieldclass'})

class OrderEditForm(ModelForm):
    class Meta:
        model = Order
        fields='__all__'
        exclude = ['master_send_sms', 'master_changed']
        widgets = {
            'work': SelectMultiple()
        }