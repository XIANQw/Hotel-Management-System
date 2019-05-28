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
        taille = request.POST.get("taille")
        users = Client.objects.all()
        res = Ressource.objects.filter(numero=numero)
        if res:
            info = "Cette ressource est deja existe"
        else:
            info = "Nouvelle ressource est bien cree"
            infoType = 'success'
            Ressource.objects.create(numero=numero, prix=prix,type=type,taille=taille)
    res = Ressource.objects.all()
    return render(request, 'gestionnaire.html', {'res': res,'info': info,'infoType':infoType})

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
        concer_meu = Concerne_Meuble.objects.filter(ressource = res)
        toutMeu = Meuble.objects.all()
        meu = []
        for i in concer_meu:
            meu.append(i.meuble)
        if res:
            return render(request,'ressource.html',{'res':res,'meu':meu,'toutMeu':toutMeu})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info,'infoType':'danger'})

def creerMeuble(request):
    info = "error"
    infoType = 'danger'
    verifier(request)
    if request.method == "POST":
        nomMeuble = request.POST.get("nomMeuble")
        status = request.POST.get("status")
        resId = request.POST.get("resId")
        Meubles = Meuble.objects.all()
        meu = Meuble.objects.filter(nom_Meuble=nomMeuble)
        res = Ressource.objects.get(id=resId)
        if meu:
            info = "Ce meuble est deja existe"
        else:
            info = "Nouveau meuble est bien crée"
            infoType = 'success'
            Meuble.objects.create(nom_Meuble=nomMeuble, status=status)
    toutMeu = Meuble.objects.all()
    return render(request, 'ressource.html', {'res':res,'toutMeu': toutMeu, 'info': info, 'infoType': infoType})


def consulterClient(request):
    verifier(request)
    if request.method == "GET":
        id = request.GET['id']
        client = Client.objects.get(id=id)
        demandes = Demande.objects.filter(client=client)
        if demandes:
            return render(request, 'clientDemande.html', {'demandes': demandes,'user':client})
    info = "error"
    infoType = 'danger'
    return render(request, 'gestionnaire.html', {'info': info,'infoType': infoType})