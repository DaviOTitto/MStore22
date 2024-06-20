from django.shortcuts import render, resolve_url, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView
from django.forms.models import inlineformset_factory
from dateutil.parser import parse
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime

import psycopg2
import tkinter as tk
from contextlib import closing
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk as itk
import cv2
import os
from matplotlib import pyplot as plt
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
import PIL.Image as Image
import MySQLdb

from ..models import *
from ..forms import *



home = TemplateView.as_view(template_name='pag2.html')
emprodu = TemplateView.as_view(template_name='emprodu.html')
def  conectaMysql():
    con = MySQLdb.connect(host='186.202.152.195',
                           database='cecotein3',
                           user='cecotein3',
                           password='vsy8y3',
                           port=3306)
    return con

SAlvo = TemplateView.as_view(template_name='SAlvo.html')
produ = TemplateView.as_view(template_name='emprodu.html')
def adciona_automatico(request):
    booleana = False
    order_forms = Pedido() 
    con_mysql = conectaMysql()
    cur_mysql = con_mysql.cursor()
    data_hora = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    data =  datetime.today().strftime("%Y/%m/%d")
    print(data)
    cur_mysql.execute ('''SELECT codped_ped 
                        FROM pedido 
                        ORDER BY  codped_ped DESC''')
    dados = cur_mysql.fetchone()
    Var = int(dados[0])
    print(Var)
    Var = Var + 1 
            #inserção de dados por backend
    sql = '''INSERT into pedido 
        (`codemp_ped`,`data_ped`,`cnpjcli_ped`,`hora_ped`,`conpag_ped`)
                values(%s,%s,%s,%s,%s)'''
    sql2 = '''INSERT into itemped 
            (`codemp_ite`,`codped_ite`,`codpro_ite`,`quantidade_ite`,`preco_ite`)
            values(%s,%s,%s,%s,%s)'''            
    lista_insert = [3,data,"51738180697",data_hora,1]                      
    lista_insert2 = [3,Var,19634,1,100.12]

    try: 
          print("entrou no try ")
          cur_mysql.execute(sql,lista_insert)
          print("executou o sql executou sql do Pedido ") 
          con_mysql.commit()
          booleana=True
    except:
          print("não foi")
          con_mysql.rollback()
          booleana=False
   
    try: 
          print("entrou no try ")
          cur_mysql.execute(sql2,lista_insert2)
          print("executou o sql  do ItemPed") 
          con_mysql.commit()
          booleana=True

    except:
          print("não foi")
          con_mysql.rollback()
          booleana=False
    if booleana : 
        return HttpResponseRedirect(resolve_url("SAlvo"))
    else :
        return HttpResponseRedirect(resolve_url("emprodu"))

def adcinona_cliente(request):
    booleana = False
    con_mysql = conectaMysql()
    cur_mysql = con_mysql.cursor()
    data_hora = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    data =  datetime.today().strftime("%Y/%m/%d")
    print(data)
            #inserção de dados por backend
    sql = '''INSERT into cliente 
        (`cpnjcpf_cli`,`nome_cli`,`endereco_cli`,`bairro_cli`,`cidade_cli`,
        `estado_cli`,`cep_cli`,`email_cli`,`telefone1_cli`,`senha_cli`,`est_civ_cli`,`índice_cli`)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
               
    lista_insert = [3,data,"51738180697",data_hora,1]                      
    order_forms = Clientes()
    if request.method == 'POST':
        forms = ClientesForm(request.POST, request.FILES,
                          instance=order_forms, prefix='main')      
  #   ESCOLHA = request.POST.get("opcaoRadio",False)
  #   print(ESCOLHA)    
  #   order_forms.escolha_radio =str(ESCOLHA)
  #   print(order_forms.escolha_radio)      
        cliente_instance.cpf = forms.cleaned_data['cpnjcpf_cli']
        cliente_instance.nome_cli = forms.cleaned_data['nome_cli']
        cliente_instance.endereco_cli = forms.cleaned_data['endereco_cli']
        cliente_instance.bairro_cli = form.cleaned_data["bairro_cli"]
        cliente_instance.cidade_cli = forms.cleaned_data['cidade_cli']
        cliente_instance.estado_cli = forms.cleaned_data['estado_cli']
        cliente_instance.cep_cli = forms.cleaned_data['cep_cli']
        cliente_instance.Email_cli = forms.cleaned_data['email_cli']
        cliente_instance.telefone1_cli = forms.cleaned_data['telefone1_cli']
        cliente_lista = [
                        cliente_instance.cpf,
                        cliente_instance.nome_cli,
                        cliente_instance.endereco_cli,
                        cliente_instance.cidade_cli,
                        cliente_instance.estado_cli,
                        cliente_instance.cep_cli,
                        cliente_instance.Email_cli,
                        cliente_instance.telefone1_cli,
                        1,5,0
                    ]
        print(cliente_lista)
        try: 
            print("entrou no try ")
            cur_mysql.execute(sql,lista_insert),
            print("executou o sql executou sql do Pedido ") 
            con_mysql.commit()
            booleana=True
        except:
            print("não foi")
            con_mysql.rollback()
            booleana=False
        if forms.is_valid() :
            teste_instance = forms.save()
       # return HttpResponseRedirect(resolve_url('detalhe_formulario',teste_instance.pk))
    else:
        forms = ClientesForm(instance=order_forms, prefix='main')
        
    context = {
        'forms': forms,
      }

    return render(request,'cadastro.html',context)
   






def completa_lista(request):
    
    if request.method == 'POST':  
        form = CadastrosForm(request.POST)
        if form.is_valid():
            form = form.save()
            #return HttpResponseRedirect(resolve_url('core:cadastros_detail', form.pk))
    else:
        form = CadastrosForm()
    context = {
        'form':form,
    }
    return render(request,'pag1.html',context)


    