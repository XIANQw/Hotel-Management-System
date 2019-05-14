from django.shortcuts import render, redirect

# Create your views here.
from gestion.models import  *

def gestionnaire(request):
    if request.session.get("username") != "root":
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info})
    res = Ressource.objects.all()
    users = Client.objects.all()
    return render(request,'gestionnaire.html',{'res':res,'users':users})

def createRessource(request):
    info = "error"
    if request.session.get("username") != "root":
        info = "Reconnectez-vous s'il vous plait"
        return render(request,"index.html",{'info':info})
    if request.method == "POST":
        numero = request.POST.get("numero")
        prix = request.POST.get("prix")
        type = request.POST.get("type")
        taille = request.POST.get("taille")
        users = Client.objects.all()
        res = Ressource.objects.filter(numero=numero)
        if res:
            info = "Cette ressource est deja existe"
        else:
            info = "Nouvelle ressource est bien cree"
            Ressource.objects.create(numero=numero, prix=prix,type=type,taille=taille)
    res = Ressource.objects.all()
    return render(request, 'gestionnaire.html', {'res': res, 'users':users, 'info': info})

def gotoModifyRes(request):
    if request.session.get("username") != "root":
        return render(request,"index.html",{'message':"Reconnectez s'il vous plait"})

    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        return render(request,'modifyRes.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info})


def modifyRessource(request):
    if request.session.get("username") != "root":
        return render(request,"index.html",{'message':"Reconnectez s'il vous plait"})
    info = "error"
    if request.method == "POST":
        id = request.POST.get("id")
        numero = request.POST.get("numero")
        prix = request.POST.get("prix")
        type = request.POST.get("type")
        taille = request.POST.get("taille")
        res = Ressource.objects.get(id=id)
        tmp = Ressource.objects.filter(numero=numero)
        if tmp and tmp[0].id != res.id:
            info = "Il a deja existe une ressource "+ numero
            return render(request,"ressource.html",{'res':res,'info':info})
        info = "Bien modifie"
        res.numero = numero
        res.prix=prix
        res.type=type
        res.taille=taille
        res.save()
    else:
        info = "Cette ressource n'existe pas"
    return render(request,"ressource.html",{'res':res,'info':info})

def deleteRessource(request):
    if request.session.get("username") != "root":
        return render(request,"index.html",{'message':"Reconnectez s'il vous plait"})
    info = "error"
    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        if res:
            info="Cette ressource est bien supprimee"
            res.delete()
        else:
            info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    users = Client.objects.all()
    return render(request, 'gestionnaire.html', {'users':users,'res': res, 'info': info})


def consulterRes(request):
    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        if res:
            return render(request,'ressource.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info})


