"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from login.views import *
from gestion.views import *
from client.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('signUp/', signUp),
    path('gestionnaire/',gestionnaire),
    path('createRessource/', createRessource),
    path('consulterRes/', consulterRes),
    path('consulterRes/modifyRessource/',gotoModifyRes),
    path('modifyRes/',modifyRessource),
    path('consulterRes/deleteRessource/',deleteRessource),
    path('consulterRes/creerMeuble/',creerMeuble),
    path('mainPage/',mainPage),
    path('consulterProfile/',consulterProfile),
    path('logout/',logout),
    path('gotoModifyAccount/',gotoModifyAccount),
    path('modifyCompte/',modifyCompte),
    path('createDemande/',createDemande),
    path('consulterClient/',consulterClient),
    path('consulterDemande/',consulterDemande),
]