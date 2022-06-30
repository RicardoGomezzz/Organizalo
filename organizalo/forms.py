
from dataclasses import fields
from django.db import models
from django import forms
from .models import Transaccion

from organizalo.models import Transaccion


class TranscForm (forms.ModelForm):
    class Meta:
        models = Transaccion
        fields = '__all__'