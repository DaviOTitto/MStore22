from django import forms

from .models import *
from rest_framework import serializers
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from .models.dados import * 

class  CadastrosForm(forms.ModelForm):
    class Meta:
        model =  Contactar
        fields = '__all__'