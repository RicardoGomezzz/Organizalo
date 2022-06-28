
from dataclasses import fields
from django.db import models
from django import forms
from .models import Transaccion

from organizalo.models import Transaccion


class FormularioTransaccion (forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = Transaccion
=======
        models = Transaccion
>>>>>>> e9f7098e78f2df6f9ed95f1b15770ee570354f90
        fields = '__all__'
        widgets = ()