from django.shortcuts import render, redirect

# Create your views here.
from gestion.models import  *

def verifier(request):
    if request.session.get("username") != "root":
        infoType='warning'
        info = "Reconnectez s'il vous plait"
        return render(request,"index.html",{'info':info,'infoType':infoType})


def gestionnaire(request):
    verifier(request)
    res = Ressource.objects.all()
    users = Client.objects.all()
    demandes = Demande.objects.all()
    return render(request,'gestionnaire.html',{'res':res, 'users':users,'demandes':demandes})


def createRessource(request):
    info = "error"
    infoType = 'danger'
    verifier(request)
    if request.method == "POST":
        numero = request.POST.get("numero")
        prix = request.POST.get("prix")
        type = request.POST.get("type")
        res = Ressource.objects.filter(numero=numero)
        if res:
            info = "Cette ressource est deja existe"
        else:
            info = "Nouvelle ressource est bien cree"
            infoType = 'success'
            if type == "Chambre":
                taille = request.POST.get('taille')
                niveau = request.POST.get('niveau')
                fumeur = request.POST.get('fumeur')
                Ressource.objects.create(numero=numero, prix=prix,type="{}-{} {}-{}".format(niveau,type,taille,fumeur))
            else:
                taille = request.POST.get('tailleSDC')
                Ressource.objects.create(numero=numero,prix=prix,type="{} {}".format(taille,type))
    res = Ressource.objects.all()
    users = Client.objects.all()
    return render(request, 'gestionnaire.html', {'res': res,'user':users,'info': info,'infoType':infoType})

def gotoModifyRes(request):
    verifier(request)
    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        return render(request,'modifyRes.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info,'infoType':'danger'})


def modifyRessource(request):
    verifier(request)
    if request.method == "POST":
        id = request.POST.get("id")
        numero = request.POST.get("numero")
        prix = request.POST.get("prix")
        type = request.POST.get("type")
        res = Ressource.objects.get(id=id)
        tmp = Ressource.objects.filter(numero=numero)
        if tmp and tmp[0].id != res.id:
            info = "Il a deja existe une ressource "+ numero
            infoType = "danger"
            return render(request,"ressource.html",{'res':res,'info':info,'infoType':infoType})
        info = "Bien modifie"
        infoType = "success"
        res.numero = numero
        res.prix = prix
        if type == "Chambre":
            taille = request.POST.get('taille')
            niveau = request.POST.get('niveau')
            fumeur = request.POST.get('fumeur')
            res.type = "{}-{} {}-{}".format(niveau,type,taille,fumeur)

        else:
            taille = request.POST.get('tailleSDC')
            res.type = "{} {}".format(taille,type)
        res.save()
    return render(request,"ressource.html",{'res':res,'info':info,'infoType':infoType})


def deleteRessource(request):
    verifier(request)
    info = "error"
    infoType = 'danger'
    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        if res:
            info="Cette ressource est bien supprimee"
            infoType = 'success'
            res.delete()
        else:
            info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    return render(request, 'gestionnaire.html', {'res':res,'infoType': infoType, 'info': info})


def consulterRes(request):
    verifier(request)
    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)

        return render(request,'ressource.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info,'infoType':'danger'})


