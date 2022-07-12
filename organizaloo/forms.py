from django import forms
from .models import Transaccion, Contacto

class TransaccionForm(forms.ModelForm):
    
    
    class Meta:
        model = Transaccion
        fields = '__all__'
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'