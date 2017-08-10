from django.forms import ModelForm
from .models import *

class MasterAddForm(ModelForm):
    class Meta:
        model = Master
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MasterAddForm, self).__init__(*args, **kwargs)
        for myfield in self.fields:
            self.fields[myfield].widget.attrs['class'] = 'form-control'
        self.fields['contract'].widget.attrs.update({'class': 'myfieldclass'})
        self.fields['zamer'].widget.attrs.update({'class': 'myfieldclass'})
        self.fields['profession'].widget.attrs.update({'id': 'category'})
        self.fields['work'].widget.attrs.update({'id': 'subcategory'})


