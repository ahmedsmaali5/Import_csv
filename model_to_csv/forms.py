from .models import *
from django import forms
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','last_name']
