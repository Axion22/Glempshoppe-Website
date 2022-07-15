from django.forms import ModelForm
from django import forms
from .models import *

class BookAppointmentForm(forms.ModelForm):
  class Meta:
    model = BookAppointment
    fields = '__all__'
    widgets = {
      'first_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':"First Name", 'required':True }),
      'last_name': forms.TextInput(attrs = {'class':'form-control' }),
      'phone': forms.TextInput(attrs = {'class':'form-control' }),
      'email': forms.TextInput(attrs = {'class':'form-control' }),
      'day': forms.TextInput(attrs = {'class':'form-control' }),
      'time': forms.TextInput(attrs = {'class':'form-control' }),
      'service': forms.TextInput(attrs = {'class':'form-control' }),
      'message': forms.Textarea(attrs = {'class':'form-control' }),
    }