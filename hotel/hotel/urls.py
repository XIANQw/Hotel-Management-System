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
    # ------------------gestionnaire------------------------------------------------
    path('gestionnaire/', gestion.views.gestionnaire),
    path('gestionnaire/createRessource/', gestion.views.createRessource),
    path('gestionnaire/consulterRes/', gestion.views.consulterRes),
    path('gestionnaire/consulterRes/modifyRessource/', gestion.views.gotoModifyRes),
    path('gestionnaire/modifyRes/', gestion.views.modifyRessource),
    path('gestionnaire/consulterRes/deleteRessource/', gestion.views.deleteRessource),
    path('gestionnaire/consulterRes/creerMeuble/', gestion.views.creerMeuble),
    path('gestionnaire/consulterRes/ajouterMeu/', gestion.views.ajouterMeuble),
    path('gestionnaire/consulterRes/removeMeu/', gestion.views.removeMeuble),
    path('gestionnaire/redirectToSuccessfulAdd/', gestion.views.redirectToSuccessfulAdd),
    path('gestionnaire/consulterClient/', gestion.views.consulterClient),
    path('gestionnaire/listDemandes/', gestion.views.listDemandes),
    path('gestionnaire/listClients/', gestion.views.gotoListClients),
    path('gestionnaire/consulterDemande/', client.views.consulterDemande),
    path('gestionnaire/accepterDemande/', gestion.views.accepterDemande),
    path('gestionnaire/consulterRes/modifMeuble/', gestion.views.modifMeuble),
    path('gestionnaire/consulterRes/deleteMeu/', gestion.views.deleteMeuble),
    path('gestionnaire/consulterRes/consultPlanRessource/', gestion.views.consultPlanRessource),
    path('gestionnaire/consulterRes/consulterDemRes/', gestion.views.consulterDemRes),
    path('gestionnaire/refuserDemande/',gestion.views.refuserDemande),

    # --------------------------client----------------------------------------------
    path('mainPage/', client.views.mainPage),
    path('mainPage/consulterProfile/', client.views.consulterProfile),
    path('mainPage/gotoModifyAccount/', client.views.gotoModifyAccount),
    path('mainPage/modifyCompte/', client.views.modifyCompte),
    path('mainPage/createDemande/', client.views.createDemande),
    path('mainPage/consulterDemande/', client.views.consulterDemande),
    path('mainPage/myDemandes/', client.views.myDemandes),
    path('mainPage/consulterRes/', client.views.consulterRes),
    path('mainPage/consulterRes/consultPlanRessource/', client.views.consultPlanRessource),

    path('deleteDemande/', client.views.deleteDemande),

]
