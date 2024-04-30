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


class Pedido(models.Model):
    codped_ped = models.AutoField("Codigo",primary_key=True)
    cnpj = models.CharField("cnpj",max_length=14,null=True ,blank =True)
    hora_ped = models.DateTimeField("Data e hora ",null=True ,blank =True,auto_now_add=True,auto_now=False)
   
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
class ItemPed(models.Model):
    coditem_ite = models.AutoField("Codigo",primary_key=True)
    Código_da_empresa = models.IntegerField("codigo da empresa",null=True)
    Código_do_produto = models.IntegerField("codigo do produto",null=True)
    Quantidade = models.IntegerField("quantidade",null=True)
    Preço = models.DecimalField("valor do produto", null =True , max_digits=6,decimal_places=2)
    class Meta:
        verbose_name ="item pedido"
        verbose_name_plural = "itens pedidos"