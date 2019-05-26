from django.shortcuts import render
from login.models import *
from gestion.models import *
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
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        nb = request.POST.get("nb")
        client = Client.objects.get(login=request.session.get("username"))
        infoType = "danger"
        checkin = datetime.datetime.strptime(checkin,"%Y-%m-%d").date()
        checkout = datetime.datetime.strptime(checkout,"%Y-%m-%d").date()
        if checkin<datetime.date.today():
            info = "date de checkin ne peut pas etre inferieur a aujoud'hui"
        elif checkin>=checkout:
            info = "date de checkin doit etre inferieur a celle de checkout"
        else:
            info = "Merci de votre demande !"
            infoType="success"
            Demande.objects.create(checkin=checkin,checkout=checkout,nbPerson=nb,client=client)
        demandes = Demande.objects.filter(client=client)
        return render(request,'mainPage.html',{'info':info,'infoType':infoType,'demandes':demandes})