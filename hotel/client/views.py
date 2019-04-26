from django.shortcuts import render
from login.models import *
# Create your views here.
def modifyCompte(request):
    info = "error"
    if request.method == "POST":
        pwd = request.POST.get("pwd")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        adresse = request.POST.get("adresse")
        tel = request.POST.get("tel")
        users = Client.objects.filter(login=login)
        if users:
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
