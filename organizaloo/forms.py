from django import forms
from .models import Transaccion, Contacto
from .models import Transaccion
from django.contrib.auth.forms import UserCreationForm

class TransaccionForm(forms.ModelForm):
    
    
    class Meta:
        model = Transaccion
        fields = '__all__'
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass
