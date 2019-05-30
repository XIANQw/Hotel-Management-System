from django.shortcuts import render,redirect

# Create your views here.
from gestion.models import  *


def gestionnaire(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request,"index.html",{'info':info,'infoType':infoType})

    res = Ressource.objects.all()
    return render(request,'gestionnaire.html',{'res':res})

def gotoListClients(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    users = Client.objects.all()
    return render(request,'listClients.html',{'users':users})

def listDemandes(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})
    flag = request.GET['flag']
    if flag == '1':
        demandes = Demande.objects.all()
    elif flag == '2':
        demandes = Demande.objects.filter(status='attendu')
    else:
        demandes = Demande.objects.filter(status='accepte')
    return render(request,'listDemandes.html',{'demandes':demandes,'flag':flag})


def createRessource(request):
    info = "error"
    infoType = 'danger'
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

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
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        return render(request,'modifyRes.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info,'infoType':'danger'})


def modifyRessource(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

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
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    info = "error"
    infoType = 'danger'
    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        meu = consulInfoRes(request,res)
        meubles = Meuble.objects.filter(status='disponible')
        if meu:
            info = "Tu dois supprimer touts les meubles de ce ressource"
            return render(request, 'ressource.html', {'res': res, 'resMeu': meu, 'meubles': meubles,'info': info, 'infoType': infoType})
        else:
            if res:
                info="Cette ressource est bien supprimee"
                infoType = 'success'
                res.delete()
            else:
                info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    return render(request, 'gestionnaire.html', {'res':res,'infoType': infoType, 'info': info})

def consulInfoRes(request,ressource):
    concer_meu = Concerne_Meuble.objects.filter(ressource=ressource)
    meu = []
    for i in concer_meu:
        meu.append(i.meuble)
    return meu


def consulterRes(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        resMeu = consulInfoRes(request,res)
        meubles = Meuble.objects.filter(status="disponible")
        if res:
            return render(request,'ressource.html',{'res':res,'resMeu':resMeu,'meubles':meubles})
        return render(request,'ressource.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info,'infoType':'danger'})

def creerMeuble(request):

    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "POST":
        nomMeuble = request.POST.get("nomMeuble")
        resId = request.POST.get("resId")
        Meuble.objects.create(nom_Meuble=nomMeuble, status="disponible")

    return redirect('/gestionnaire/redirectToSuccessfulAdd/?resId='+resId)

def ajouterMeuble(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})


    if request.method == "GET":
        resId = request.GET['resId']
        meuId = request.GET['meuId']
        res = Ressource.objects.get(id=resId)
        meuble = Meuble.objects.get(id=meuId)
        meuble.status = 'occupé'
        meuble.save()
        Concerne_Meuble.objects.create(ressource=res, meuble=meuble)
    return redirect('/gestionnaire/redirectToSuccessfulAdd/?resId='+resId)


def removeMeuble(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        resId = request.GET['resId']
        meuId = request.GET['meuId']
        res = Ressource.objects.get(id=resId)
        meuble = Meuble.objects.get(id=meuId)
        meuble.status = 'disponible'
        meuble.save()
        ConcerMeuble = Concerne_Meuble.objects.get(ressource=res, meuble=meuble)
        if ConcerMeuble.delete():
            info = "ce meuble est bien remove"
            infoType = 'success'
        return redirect('/gestionnaire/redirectToSuccessfulAdd/?resId=' + resId)

def modifMeuble(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "POST":
        resId = request.POST['resId']
        meuId = request.POST['meuId']
        nomMeu = request.POST['meuNom']
        meuble = Meuble.objects.get(id=meuId)
        if meuble:
            meuble.nom_Meuble = nomMeu
            meuble.save()
    return redirect('/gestionnaire/redirectToSuccessfulAdd/?resId=' + resId)

def deleteMeuble(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        resId = request.GET['resId']
        meuId = request.GET['meuId']
        meuble = Meuble.objects.get(id=meuId)
        meuble.delete();

        return redirect('/gestionnaire/redirectToSuccessfulAdd/?resId=' + resId)

def redirectToSuccessfulAdd(request):
    info = "Nouveau meuble est bien ajouté"
    infoType = "success"
    if request.method == "GET":
        resId = request.GET['resId']
        res = Ressource.objects.get(id=resId)
        resMeu = consulInfoRes(request, res)
        meubles = Meuble.objects.filter(status="disponible")
    return render(request,'ressource.html',{'res': res, 'resMeu': resMeu, 'meubles': meubles, 'info': info, 'infoType': infoType})


def consulterClient(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        id = request.GET['id']
        flag = request.GET['flag']
        client = Client.objects.get(id=id)
        if flag == '1':
            demandes = Demande.objects.filter(client=client)
        elif flag == '2':
            demandes = Demande.objects.filter(client=client,status='attendu')
        else:
            demandes = Demande.objects.filter(client=client,status='accepte')
        if demandes:
            return render(request, 'clientDemande.html', {'demandes': demandes,'user':client,'flag':flag})
        else:
            info = "Ce client n'a aucune de demande"
            return render(request,'clientDemande.html',{'info':info,'user':client,'flag':flag})
    info = "error"
    infoType = 'danger'
    return render(request, 'gestionnaire.html', {'info': info,'infoType': infoType})
