from django.shortcuts import render,redirect
from login.models import *
from gestion.models import *
from django.core.exceptions import ObjectDoesNotExist
import datetime
# Create your views here.

def checkSession(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info, 'infoType':'warning'})

def mainPage(request):
    checkSession(request)
    login = request.session.get('username')
    info = "Bienvenue notre VIP " + login
    me = Client.objects.get(login=login)
    demandes = Demande.objects.filter(client=me)
    return render(request,'mainPage.html',{'info':info,'infoType':'success','demandes':demandes})


def consulterProfile(request):
    checkSession(request)
    user = Client.objects.get(login=request.session.get('username'))
    return render(request,'profile.html',{'user':user})


def gotoModifyAccount(request):
    checkSession(request)
    login = request.session.get("username")
    user = Client.objects.get(login=login)
    return render(request,'modifyAccount.html',{'user':user})


def modifyCompte(request):
    checkSession(request)
    if request.method == "POST":
        login = request.session.get("username")
        pwd = request.POST.get("pwd")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        tel = request.POST.get("tel")
        users = Client.objects.filter(login=login)
        if users:
            infoType="success"
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
    return render(request, 'mainPage.html', {'res': res, 'info': info,'infoType':infoType})

def createDemande(request):
    checkSession(request)
    if request.method == "POST":
        nbPlan = int(request.POST.get("nbPlan"))
        forms = []
        for i in range(1,nbPlan+1):
            checkin = datetime.datetime.strptime(request.POST.get("checkin"+str(i)),"%Y-%m-%d").date()
            checkout = datetime.datetime.strptime(request.POST.get("checkout"+str(i)), "%Y-%m-%d").date()
            nb = request.POST.get("nb" + str(i))
            forms.append([checkin,checkout,nb])
        client = Client.objects.get(login=request.session.get("username"))
        infoType = "danger"
        for i in range(len(forms)):
            if forms[i][0] < datetime.date.today():
                demandes = Demande.objects.filter(client=client)
                info = "Erreur sur plan{} : date de checkin ne peut pas etre inferieur a aujoud'hui".format(i+1)
                return render(request, 'mainPage.html', {'info': info, 'infoType': infoType, 'demandes': demandes})
            elif forms[i][0] >= forms[i][1]:
                demandes = Demande.objects.filter(client=client)
                info = "Erreur sur plan{} : date de checkin doit etre inferieur a celle de checkout".format(i+1)
                return render(request, 'mainPage.html', {'info': info, 'infoType': infoType, 'demandes': demandes})
        try:
            numero = Demande.objects.filter(client=client).latest('numero').numero+1
        except ObjectDoesNotExist:
            numero =1
        demande = Demande.objects.create(numero=numero,client=client)
        for i in range(len(forms)):
            plan = Plan.objects.create(numero= i+1, checkin=forms[i][0], checkout=forms[i][1], nbPerson=forms[i][2], owner=client)
            DemandePlan.objects.create(demande=demande,plan=plan)
        info = "Merci de votre demande !"
        infoType ="success"
        demandes = Demande.objects.filter(client=client)
        return render(request,'mainPage.html',{'info':info,'infoType':infoType,'demandes':demandes})


def consulterDemande(request):
    checkSession(request)
    if request.method == "GET":
        id = request.GET['id']
        demande = Demande.objects.get(id=id)
        demandePlans = DemandePlan.objects.filter(demande=demande)
        plans = []
        for i in demandePlans:
            plans.append(i.plan)
        if plans:
            print(plans)
            return render(request,'demande.html',{'plans':plans})
    return redirect('/mainPage/')