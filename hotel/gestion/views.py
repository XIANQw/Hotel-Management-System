from django.shortcuts import render

# Create your views here.
from login.models import *
from gestion.models import  *

def createRessource(request):
    info = "error"
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

def modifyRessource(request):
    info = "error"
    if request.method == "POST":
        numero = request.POST.get("numero")
        prix = request.POST.get("prix")
        type = request.POST.get("type")
        taille = request.POST.get("taille")
        res = Ressource.objects.filter(numero=numero)
        if res:
            info = "Bien modifie"
            res[0].prix=prix
            res[0].type=type
            res[0].taille=taille
            res[0].save()
        else:
            info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    users = Client.objects.all()
    return render(request, 'gestionnaire.html', {'users':users,'res': res, 'info': info})
