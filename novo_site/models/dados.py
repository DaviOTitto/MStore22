import uuid
import re
from django.db import models
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, resolve_url, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils.formats import number_format
from django.utils import timezone
from simplecep import resolve_cep


from . import *
from datetime import datetime
class Clientes(models.Model):
    options_choices = (
        ('M', ' Masculino '),
        ('F', 'Feimino '),
    )
    cpf = models.CharField("cpf",primary_key=True,max_length=11)
    nome_cli = models.CharField("nome",max_length=200,null=True)
    endereco_cli = models.CharField("endereco",max_length=200,null=True)
    cidade_cli = models.CharField("cidade",max_length=200,null=True)
    bairro_cli= models.CharField("bairro",max_length=200,null=True)
    estado_cli= models.CharField("estado silga",max_length=2,null=True)
    cep_cli = models.CharField("cep",max_length=10,null=True)
    Email_cli = models.CharField("email",max_length=200,null=True)
    telefone1_cli = models.CharField("telefone",max_length=11,null=True)
    sexo_cli = models.CharField("sexo",max_length=1,choices=options_choices)
    class Meta:
        verbose_name="cliente"
        verbose_name_plural="clientes"

    
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