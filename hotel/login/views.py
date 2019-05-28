from django.shortcuts import render, redirect
from gestion.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')


def signUp(request):
    info = "error"
    infoType = "danger"
    if request.method == "POST":
        login = request.POST.get("email").strip()
        pwd = request.POST.get("pwd").strip()
        nom = request.POST.get("nom").strip()
        prenom = request.POST.get("prenom").strip()
        email = request.POST.get("email").strip()
        adresse = request.POST.get("adresse").strip()
        tel = request.POST.get("tel").strip()
        users = Client.objects.filter(login=login)
        if users:
            info = "Compte existe"
        else:
            info = "Nouveau utilisateur est bien enregistre"
            infoType = "success"
            # save Client in database
            Client.objects.create(login=login, pwd=pwd,nom=nom,prenom=prenom,email=email,adresse=adresse,tel=tel)
    # read data from database
    res = Ressource.objects.all()
    return render(request, 'index.html', {'res': res, 'info': info,'infoType':infoType})


def login(request):
    if request.method == "POST":
        infoType = "danger"
        login = request.POST.get("login")
        pwd = request.POST.get("pwd")
        if login == "root":
            ro = Gestionnaire.objects.get(login="root")
            if ro.pwd == pwd:
                info = "Bienvenue, gestionnaire"
                infoType = "success"
                res = Ressource.objects.all()
                request.session["username"] = login
                return render(request,'gestionnaire.html',{'info':info,'res':res,'infoType':infoType})
            else:
                info = "votre mot de pass n'est pas correct"
                return render(request, 'index.html', {'info': info,'infoType':infoType})
        user = Client.objects.filter(login=login)
        if user:
            if user[0].pwd != pwd:
                info = "votre mot de pass n'est pas correct"
            else:
                info = "Bienvenue notre VIP " + user[0].nom
                infoType = "success"
                request.session["username"] = login
                return render(request, 'mainPage.html', {'info': info,'infoType':infoType})
        else:
            info = "This profile do not exist"
    return render(request,'index.html',{'info':info,'infoType':infoType})


def logout(request):
    request.session.flush()
    return redirect("/index/")



