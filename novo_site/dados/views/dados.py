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

from ..models import *
from ..forms import *



home = TemplateView.as_view(template_name='pag2.html')
emprodu = TemplateView.as_view(template_name='emprodu.html')
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


    