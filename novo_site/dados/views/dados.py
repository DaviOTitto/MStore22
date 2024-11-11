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
from simplecep import resolve_cep
from ..models import *
from ..forms import *
import brazilcep 
#from pycep_correios import consultar_cep
import time

home = TemplateView.as_view(template_name='pag2.html')
emprodu = TemplateView.as_view(template_name='emprodu.html')
teste = TemplateView.as_view(template_name='pesquisa_cpf.html')
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
                      
    order_forms = Clientes()
    query = '''Select cpnjcpf_cli,nome_cli,endereco_cli,
        bairro_cli,cidade_cli,estado_cli,
        cep_cli,email_cli,telefone1_cli,
        senha_cli,est_civ_cli,indice_cli,
        sexo_cli from cliente  where cnpjcpf_cli = %s'''
    existing_client = None 
    if request.method == 'POST':
        forms = ClientesForm(request.POST, request.FILES,
                          instance=order_forms, prefix='main')          
        if forms.is_valid() :
            print("ENTROU NO FORM IS VALID")
            print("Print aqui " + str(request.POST.get('id_main-cpf'),))
            con_mysql.execute(query, (request.POST.get('id_main-cpf'),))
            
            #query.execute = (query,(request.POST.get('main-cpf'),))
            existing_client = cur_mysql.fetchone()
          #  var = existing_client[0]
            print("print testa " + str(existing_client))  # Corrigido para str(existing_client)
            if existing_client : 
                print ("cliente ja existe")
            else :
                forms.save()              
                cliente_lista = listar_clientes(request)
                print(cliente_lista)   
           # if forms.is_valid() :
           #     print("form valido")
           #      forms.save()
            #    cliente_lista = listar_clientes(request)
            #    print(cliente_lista)     

                       
    else:
        forms = ClientesForm(instance=order_forms, prefix='main')
        print("ta no else ")
        
    context = {
        'forms': forms,
      }
    return render(request,'cadastro.html',context)
def pesquisa_cpf(request):
    con_mysql = conectaMysql()
    cur_mysql = con_mysql.cursor()
                      
    order_forms = Clientes()
    query = '''Select cpnjcpf_cli,nome_cli,endereco_cli,
        bairro_cli,cidade_cli,estado_cli,
        cep_cli,email_cli,telefone1_cli,
        senha_cli,est_civ_cli,indice_cli,
        sexo_cli from cliente  where cnpjcpf_cli = %s'''
    existing_client = None 
    if forms.is_valid() :
            print("ENTROU NO FORM IS VALID")
            print("Print aqui " + str(request.POST.get('id_main-cpf'),))
            con_mysql.execute(query, (request.POST.get('id_main-cpf'),))
            
            #query.execute = (query,(request.POST.get('main-cpf'),))
            existing_client = cur_mysql.fetchone()
          #  var = existing_client[0]
            print("print testa " + str(existing_client))  # Corrigido para str(existing_client)
            if existing_client : 
                print ("cliente ja existe")
            else :                            
                print(existing_client)
    return render(request,'pesquisa_cpf.html',context)





def listar_clientes(request):
    # Busque todos os registros do modelo Clientes
    ultimo_cliente = Clientes.objects.last()
    con_mysql = conectaMysql()
    cur_mysql = con_mysql.cursor()
    data_hora = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    data =  datetime.today().strftime("%Y/%m/%d")
   

    
    
    sql = '''INSERT into cliente 
        (`cpnjcpf_cli`,`nome_cli`,`endereco_cli`,
        `bairro_cli`,`cidade_cli`,`estado_cli`,
        `cep_cli`,`email_cli`,`telefone1_cli`,
        `senha_cli`,`est_civ_cli`,`indice_cli`,
        `sexo_cli`)
                values(%s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s,%s,%s,
                %s)'''
               
    print(data)
    # Crie uma lista para armazenar os dados
    

    # Itere sobre os registros e pegue os valores dos campos
    for cliente in ultimo_cliente:
        # Acesse os valores dos campos individualmente
        cpf = cliente.cpf
        nome = cliente.nome_cli
        endereco = cliente.endereco_cli
        cidade = cliente.cidade_cli
        bairro = cliente.bairro_cli
        estado = cliente.estado_cli
        cep = cliente.cep_cli
        email = cliente.Email_cli
        telefone = cliente.telefone1_cli
        aux1 = 1
        aux2 = 5
        aux3 = 1
        sexo_cli = cliente.sexo_cli
        lista_clientes = [cpf,nome,endereco,cidade,bairro,estado,cep,email,telefone,aux1,aux2,aux3,sexo_cli]
        #endereco_test = resolve_cep(cep)
       
        # Insira o CEP desejado
        #endereco = consultar_cep(cep)
        # Adicione os valores à lista
        print(lista_clientes)
       # query.execute = (query,(cpf,))
        testa_clientes = cur_mysql.fetchone()
       
        address = brazilcep.get_address_from_cep(cep)
        time.sleep(100)
        if address:
            street = address.get("street", "")
            district = address.get("district", "")
            estado = address.get("uf", "")
            print('rua' + street)
            print('bairro' + district)
            print('estado' +  estado)
            try: 
                print("entrou no try ")
                cur_mysql.execute(sql,lista_clientes )
                print("executou o sql executou sql do Pedido ") 
                con_mysql.commit()
                booleana=True
            except :
                print("não foi")
                con_mysql.rollback()
                booleana=False
                lista_clientes.clear()
        

    # Agora você tem uma lista com os dados dos clientes
    # Cada item da lista é um dicionário com os campos e valores correspondentes

    return lista_clientes
    

   






def completa_lista(request):
    
    if request.method == 'POST':  
        form = Clientes(request.POST)
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect(resolve_url('core:cadastros_detail', form.pk))
    else:
        form = Clientes()
    context = {
        'form':form,
    }
    return render(request,'pag1.html',context)


    