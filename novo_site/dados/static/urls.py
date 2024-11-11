"""
URL configuration for novo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin




from .views.dados  import *

dados_patterns = [
    path('',completa_lista,name='completa_list'),
    path('emprodu/',emprodu,name='emprodu'),
    path("rodar/",adciona_automatico,name="insert"),
    path("Salvo/",SAlvo,name="SAlvo"),
    path("emprodu/",emprodu,name="emprodu"),
    path("teste/",teste,name="teste"),
    path("insert/",adciona_automatico,name="adciona"),
    path("adciona_cli/",adcinona_cliente,name="adciona_cli")
]
urlpatterns = [
    path('', home, name='inicio'),
    path('admin/', admin.site.urls),
    path('dados/', include(dados_patterns)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
