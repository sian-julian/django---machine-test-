from django import forms
from .models import *

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields=[
            'first_name','last_name','email','department','designation','date_of_joining','salary','image'
        ]