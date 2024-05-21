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
    Var = Var +1 
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


    