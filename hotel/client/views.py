from django.shortcuts import render
from login.models import *
from gestion.models import *
# Create your views here.



def mainPage(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info})
    info = "Bienvenue notre VIP " + request.session.get('username')
    return render(request,'mainPage.html',{'info':info})



def consulterProfile(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info})
    user = Client.objects.get(login=request.session.get('username'))
    return render(request,'profile.html',{'user':user})



def gotoModifyAccount(request):
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info})
    login = request.session.get("username")
    user = Client.objects.get(login=login)
    return render(request,'modifyAccount.html',{'user':user})



def modifyCompte(request):
    info = "error"
    if not request.session.get("username", None):
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info})
    if request.method == "POST":
        login = request.session.get("username")
        pwd = request.POST.get("pwd")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        tel = request.POST.get("tel")
        users = Client.objects.filter(login=login)
        if users:
            info = "Bien modifie"
            users[0].pwd = pwd
            users[0].nom = nom
            users[0].prenom = prenom
            users[0].adresse = adresse
            users[0].tel = tel
            users[0].save()
        else:
            info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    users = Client.objects.all()
    return render(request, 'mainPage.html', {'users':users,'res': res, 'info': info})
