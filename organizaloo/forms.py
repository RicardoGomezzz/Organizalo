from django import forms
from .models import Transaccion
from django.contrib.auth.forms import UserCreationForm

class TransaccionForm(forms.ModelForm):
    
    
    class Meta:
        model = Transaccion
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass