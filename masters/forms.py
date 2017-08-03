from django.forms import ModelForm
from .models import *

class MasterAddForm(ModelForm):
    class Meta:
        model = Master
        fields = '__all__'