
from dataclasses import fields
from django.db import models
from django import forms

from organizalo.models import Transaccion


class FormularioTransaccion (forms.ModelForm):
    class Meta:
        models = Transaccion
        fields = '__all__'
        widgets = ()