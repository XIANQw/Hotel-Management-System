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
import login.views
import gestion.views
import client.views
import client.views
import gestion.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', login.views.index),
    path('login/', login.views.login),
    path('signUp/', login.views.signUp),
    path('logout/', login.views.logout),

    path('gestionnaire/', gestion.views.gestionnaire),
    path('gestionnaire/createRessource/', gestion.views.createRessource),
    path('gestionnaire/consulterRes/', gestion.views.consulterRes),
    path('gestionnaire/consulterRes/modifyRessource/',gestion.views.gotoModifyRes),
    path('gestionnaire/modifyRes/',gestion.views.modifyRessource),
    path('gestionnaire/consulterRes/deleteRessource/',gestion.views.deleteRessource),
    path('gestionnaire/consulterRes/creerMeuble/',gestion.views.creerMeuble),
    path('gestionnaire/consulterClient/', gestion.views.consulterClient),
    path('gestionnaire/listDemandes/', gestion.views.gotoListDemandes),
    path('gestionnaire/listClients/',gestion.views.gotoListClients),
    path('gestionnaire/consulterDemande/', client.views.consulterDemande),

    path('mainPage/',client.views.mainPage),
    path('mainPage/consulterProfile/', client.views.consulterProfile),
    path('mainPage/gotoModifyAccount/',client.views.gotoModifyAccount),
    path('mainPage/modifyCompte/',client.views.modifyCompte),
    path('mainPage/createDemande/',client.views.createDemande),
    path('mainPage/consulterDemande/',client.views.consulterDemande),
    path('mainPage/listDemandes/',client.views.gotoListDemandes),
]