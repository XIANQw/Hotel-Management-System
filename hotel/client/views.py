from django.shortcuts import render, redirect
from login.models import *
from gestion.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

import datetime


# Create your views here.


def mainPage(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    login = request.session.get('username')
    info = "Bienvenue notre VIP " + login

    return render(request, 'mainPage.html', {'info': info, 'infoType': 'success'})


def consulterProfile(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    user = Client.objects.get(login=request.session.get('username'))
    return render(request, 'profile.html', {'user': user})


def myDemandes(request):
    if not request.session.get("username", None) or request.session.get('id') != int(request.GET['id']):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})
    if request.method == "GET":
        id = request.GET['id']
        flag = request.GET['flag']
        client = Client.objects.get(id=id)
        if flag == '1':
            demandes = Demande.objects.filter(client=client)
        elif flag == '2':
            demandes = Demande.objects.filter(client=client, status='attendu')
        else:
            demandes = Demande.objects.filter(client=client, status='accepte')
        if demandes:
            return render(request, 'clientDemande.html', {'demandes': demandes, 'user': client, 'flag': flag})
        else:
            info = "Ce client n'a aucune de demande"
            return render(request, 'clientDemande.html', {'info': info, 'user': client, 'flag': flag})
    info = "error"
    infoType = 'danger'
    return render(request, 'gestionnaire.html', {'info': info, 'infoType': infoType})


def gotoModifyAccount(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    login = request.session.get("username")
    user = Client.objects.get(login=login)
    return render(request, 'modifyAccount.html', {'user': user})


def modifyCompte(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    if request.method == "POST":
        login = request.session.get("username")
        pwd = request.POST.get("pwd")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        tel = request.POST.get("tel")
        users = Client.objects.filter(login=login)
        if users:
            infoType = "success"
            info = "Bien modifie"
            users[0].pwd = pwd
            users[0].nom = nom
            users[0].prenom = prenom
            users[0].adresse = adresse
            users[0].tel = tel
            users[0].save()
        else:
            infoType = "danger"
            info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    return render(request, 'mainPage.html', {'res': res, 'info': info, 'infoType': infoType})


def createDemande(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    if request.method == "POST":
        nbPlan = int(request.POST.get("nbPlan"))
        forms = []
        for i in range(1, nbPlan + 1):
            checkin = datetime.datetime.strptime(request.POST.get("checkin" + str(i)), "%Y-%m-%d").date()
            checkout = datetime.datetime.strptime(request.POST.get("checkout" + str(i)), "%Y-%m-%d").date()
            nb = request.POST.get("nb" + str(i))
            type = request.POST.get("type" + str(i))
            if type == "Chambre":
                niveau = request.POST.get("niveau" + str(i))
                fumeur = request.POST.get("fumeur" + str(i))
                forms.append([checkin, checkout, nb, type, niveau, fumeur])
            else:
                forms.append([checkin, checkout, nb, type])
        client = Client.objects.get(login=request.session.get("username"))
        infoType = "danger"
        for i in range(len(forms)):
            if forms[i][0] < datetime.date.today():
                demandes = Demande.objects.filter(client=client)
                info = "Erreur sur plan{} : date de checkin ne peut pas etre inferieur a aujoud'hui".format(i + 1)
                return render(request, 'mainPage.html', {'info': info, 'infoType': infoType, 'demandes': demandes})
            elif forms[i][0] >= forms[i][1]:
                demandes = Demande.objects.filter(client=client)
                info = "Erreur sur plan{} : date de checkin doit etre inferieur a celle de checkout".format(i + 1)
                return render(request, 'mainPage.html', {'info': info, 'infoType': infoType, 'demandes': demandes})
        try:
            numero = Demande.objects.filter(client=client).latest('numero').numero + 1
        except ObjectDoesNotExist:
            numero = 1
        demande = Demande.objects.create(numero=numero, client=client)

        for i in range(len(forms)):
            if forms[i][3] == "Chambre":
                typeRessource = "{}-{}-{}".format(forms[i][4], forms[i][3], forms[i][5])
                plan = Plan.objects.create(numero=i + 1, checkin=forms[i][0], checkout=forms[i][1],
                                           nbPerson=forms[i][2], typeRessource=typeRessource, owner=client)
            else:
                plan = Plan.objects.create(numero=i + 1, checkin=forms[i][0], checkout=forms[i][1],
                                           nbPerson=forms[i][2], typeRessource=forms[i][3], owner=client)
            DemandePlan.objects.create(demande=demande, plan=plan)

        info = "Merci de votre demande !"
        infoType = "success"
        demandes = Demande.objects.filter(client=client)
        return render(request, 'mainPage.html', {'info': info, 'infoType': infoType, 'demandes': demandes})


def consulterDemande(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    if request.method == "GET":
        id = request.GET['id']
        cd = request.GET['cd']
        demande = Demande.objects.get(id=id)
        idc = demande.client.id
        demandePlans = DemandePlan.objects.filter(demande=demande)
        plans = []
        for i in demandePlans:
            plans.append(i.plan)
        if plans:
            return render(request, 'demande.html', {'plans': plans, 'cd': cd, 'idc': idc, 'demande': demande})
    return redirect('/mainPage/')


def deleteDemande(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    info = "error"
    infoType = "danger"
    if request.method == "GET":
        id = int(request.GET['id'])
        cd = request.GET['cd']
        demandes = Demande.objects.filter(id=id)
        if demandes:
            idc = demandes[0].client.id
            demandes[0].delete()
            info = "Cette demande est bien supprime"
            infoType = "success"
        else:
            info = "Cette demande n'existe pas"

        if cd == '-1' and request.session.get('username') == 'root':
            demandes = Demande.objects.all()
            return render(request, 'listDemandes.html',
                          {'demandes': demandes, 'info': info, 'infoType': infoType, 'flag': '1'})
        elif cd != '-1' and request.session.get('username') == 'root':
            return redirect('/gestionnaire/consulterClient/?id={}&flag=1'.format(cd))
        else:
            myId = request.session.get('id')
            me = Client.objects.get(id=myId)
            demandes = Demande.objects.filter(client=me)
            if demandes:
                return render(request, 'clientDemande.html', {'demandes': demandes, 'user': me, 'flag': '1'})
            else:
                info = "Ce client n'a aucune de demande"
                return render(request, 'clientDemande.html', {'info': info, 'user': me, 'flag': '1'})


def consulterRes(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    if request.method == "GET":
        try:
            id = request.GET['id']
        except MultiValueDictKeyError:
            id = '-1'
        planId = request.GET['planId']
        plan = Plan.objects.get(id=planId)
        resId = request.GET['resId']
        res = Ressource.objects.get(id=resId)
        resMeu = consulInfoRes(request, res)
        meubles = Meuble.objects.filter(status="disponible")
        if res:
            return render(request, 'ressource.html',
                          {'id': id, 'res': res, 'resMeu': resMeu, 'meubles': meubles, 'plan': plan})
        return render(request, 'ressource.html', {'res': res})
    info = "error"
    return render(request, 'gestionnaire.html', {'info': info, 'infoType': 'danger'})


def consulInfoRes(request, ressource):
    concer_meu = Concerne_Meuble.objects.filter(ressource=ressource)
    meu = []
    for i in concer_meu:
        meu.append(i.meuble)
    return meu


def consultPlanRessource(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': 'warning'})

    if request.method == "GET":
        try:
            id = request.GET['id']
        except MultiValueDictKeyError:
            id = '-1'
        try:
            cd = request.GET['cd']
        except MultiValueDictKeyError:
            cd = '-2'

        planId = request.GET['planId']
        flag = request.GET['flag']
        plan = Plan.objects.get(id=int(planId))
        planRessource = PlanRessource.objects.filter(plan=plan)
        res = []
        for i in planRessource:
            res.append(i.ressource)
    return render(request, 'clientRessource.html', {'id': id, 'flag': flag, 'res': res, 'cd': cd, 'plan': plan})
