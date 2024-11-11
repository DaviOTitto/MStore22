from django.contrib import admin,messages
from .models import *
from import_export.admin import ExportActionMixin,ImportExportModelAdmin
from django.urls import path
from django.shortcuts import redirect

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    ordering = ['cpf']
    list_display =('cpf','nome_cli','endereco_cli','cidade_cli','bairro_cli','estado_cli','cep_cli','Email_cli','telefone_cli','sexo_cli')
    search_fields =('cpf',)
