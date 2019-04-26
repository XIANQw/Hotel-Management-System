from django.shortcuts import render
from gestion.models import *

# Create your views here.

def index(request):
    users = Client.objects.all()
    res = Ressource.objects.all()
    return render(request,'index.html',{'users': users,'res':res })

def signUp(request):

    info = "error"
    if request.method == "POST":
        login = request.POST.get("email")
        pwd = request.POST.get("pwd")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")
        adresse = request.POST.get("adresse")
        tel = request.POST.get("tel")
        users = Client.objects.filter(login=login)
        info = ""
        if users:
            info = "user exist"
            b = True
        else:
            info = "new user was added"
            # save Client in database
            Client.objects.create(login=login, pwd=pwd,nom=nom,prenom=prenom,email=email,adresse=adresse,tel=tel)
    # read data from database
    res = Ressource.objects.all()
    return render(request, 'index.html', {'res': res, 'info': info})

def login(request):

    if request.method == "POST":
        login = request.POST.get("login")
        pwd = request.POST.get("pwd")
        res = Ressource.objects.all()
        users = Client.objects.all()
        if login == "root":
            ro = Gestionnaire.objects.get(login="root")
            if ro.pwd == pwd:
                info = "Welcome back, gestionnaire"
                return render(request,'gestionnaire.html',{'info':info,'users':users,'res':res})
        user = Client.objects.filter(login=login)
        if user:
            if user[0].pwd != pwd:
                info = "your password is not correct"
            else:
                info = "welcome back our VIP " + user[0].nom
                return render(request, 'mainPage.html', {'info': info,"user":user[0]})
        else:
            info = "This profile do not exist"
    return render(request,'index.html',{'info':info,'users':users})


