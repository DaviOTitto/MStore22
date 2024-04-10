import uuid
import re
from django.db import models
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, resolve_url, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils.formats import number_format
from django.utils import timezone


from . import *
from datetime import datetime


class Contactar(models.Model):
    id = models.AutoField("Codigo",primary_key=True)
    nome = models.CharField("name",max_length=20,null=True ,blank =True)
    email = models.CharField("email",max_length=100,null=True ,blank =True)
    mensagem = models.CharField("texto",max_length=3000,null=True ,blank =True)
   
    class Meta:
        verbose_name = 'contactar'
        verbose_name_plural = 'Contactares'