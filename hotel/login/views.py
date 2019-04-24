from django.shortcuts import render
from login import models


# Create your views here.

def index(request):
    return render(request,'index.html')

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
        users = models.Client.objects.all()
        info = ""
        b = False
        if users == []:
            for i in users:
                if i.login == login:
                    info = "user exist"
                    b = True
                    break
        if not b:
            info = "new user was added"
            # save Client in database
            models.Client.objects.create(login=login, pwd=pwd,nom=nom,prenom=prenom,email=email,adresse=adresse,tel=tel)
    # read data from database
    users = models.Client.objects.all()
    return render(request, 'index.html', {'data': users, 'info': info})

def login(request):

    if request.method == "POST":
        login = request.POST.get("login")
        pwd = request.POST.get("pwd")
        users = models.Client.objects.all()
        for tmp in users:
            if tmp.login == login:
                if tmp.pwd != pwd:
                    info = "your password is not correct"
                else:
                    info = "welcome back our VIP " + login
                    return render(request, 'mainPage.html', {'info': info})
        info = "This profile do not exist"
    return render(request,'index.html',{'info':info},{'data':users})

def create_demande(request):
    if request.method == "POST":
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        num = request.POST.get("taille")
        ressources = models.Ressource.objects.get(status="disponible")
        for i in ressources:
