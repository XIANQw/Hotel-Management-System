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
        if res:
            info="Cette ressource est bien supprimee"
            infoType = 'success'
            res.delete()
        else:
            info = "Cette ressource n'existe pas"
    res = Ressource.objects.all()
    return render(request, 'gestionnaire.html', {'res':res,'infoType': infoType, 'info': info})


def consulterRes(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        id = request.GET['id']
        res = Ressource.objects.get(id=id)
        concer_meu = Concerne_Meuble.objects.filter(ressource = res)
        meubles = Meuble.objects.all()
        meu = []
        for i in concer_meu:
            meu.append(i.meuble)
        if res:
            return render(request,'ressource.html',{'res':res,'meu':meu,'meubles':meubles})
        return render(request,'ressource.html',{'res':res})
    info = "error"
    return render(request,'gestionnaire.html',{'info':info,'infoType':'danger'})

def creerMeuble(request):
    info = "error"
    infoType = 'danger'
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "POST":
        nomMeuble = request.POST.get("nomMeuble")
        status = request.POST.get("status")
        resId = request.POST.get("resId")
        res = Ressource.objects.get(id=resId)
        meu = Meuble.objects.create(nom_Meuble=nomMeuble, status=status)
        meubles = Meuble.objects.all()
        if meu:
            info = "Nouveau meuble est bien crée"
            infoType = 'success'
    return render(request, 'ressource.html', {'res':res,'meubles': meubles, 'info': info, 'infoType': infoType})

def ajouterMeuble(request):
    return 0

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


def hasConflictDate(request,period1,period2):
    """
    Verifier si deux period ont le conflit
    :param request: request
    :param period1: list of datetime.date
    :param period2: list of datetime.date
    :return: Bool
    """
    if period1[0]<period2[0]:
        return period1[1] > period2[0]
    else:
        return period1[0] < period2[1]


def hasConflictRes(request,plan,res):
    """
    Verifier si cette ressource est disponible pour ce plan

    :param request: request
    :param plan: Plan Object
    :param res: Ressource Object
    :return: Bool
    """

    resPlan = PlanRessource.objects.filter(ressource=res)
    for i in resPlan:
        period1 = [i.checkin,i.checkout]
        period2 = [plan.checkin,plan.checkout]
        if hasConflictDate(request,period1,period2):
            return True
    return False


def chercheChambre(request,plan,size):
    """
    Chercher les ressource de size disponible pour ce plan

    :param request: request
    :param plan: Plan Object
    :param size: 'Simple','Double','Famille'
    :return: list de Ressource
    """
    types = plan.typeRessource.split("-")
    niveau = types[0]
    type = types[1]
    fumeur = types[2]
    type = "{}-{} {}-{}".format(niveau, type, size, fumeur)
    res = Ressource.objects.filter(type=type)
    resdisponible = []
    for i in res:
        if not hasConflictRes(request,plan,i):
            resdisponible.append(i)
    return resdisponible


def chercheSDC(request,plan):
    """
    chercher les SDC disponible pour ce plan

    :param request: request
    :param plan: Plan object
    :return: list de SDC disponible, list of Ressource
    """
    resDisponible = []
    if plan.nbPerson < 10:
        type = "Petite " + plan.typeRessource
    elif 10 <= plan.nbPerson < 20:
        type = "Moyenne " + plan.typeRessource
    elif 20 <= plan.nbPerson <= 30:
        type = "Grangde " + plan.typeRessource
    else:
        return None
    res = Ressource.objects.filter(type=type)
    for i in res:
        if not hasConflictRes(request, plan, i):
            resDisponible.append(i)
            return resDisponible
    return None


def chercherRes(request,plan):
    """
    Cherchez les ressources disponibles pour ce plan

    :param request:
    :param plan:
    :return:
    """
    resDisponibleD = chercheChambre(request,plan, 'Double')
    resDisponibleS = chercheChambre(request,plan,'Simple')
    resDisponibleF = chercheChambre(request,plan,'Famille')
    nbPerson = plan.nbPerson
    nbD = len(resDisponibleD)
    nbS = len(resDisponibleS)
    nbF = len(resDisponibleF)

    print('resDisponibleD:', resDisponibleD)
    print('resDisponibleS:', resDisponibleS)
    print('resDisponibleF:', resDisponibleF)
    def tmp(nbPerson,D,S,F,result):
        print('nbPerson:',nbPerson,'D:',D,'S:',S,'F:',F,'result:',result)
        if nbPerson <= 0:
            return result
        if nbD > D:
            nbPerson -= 2
            result.append(resDisponibleD[D])
            return tmp(nbPerson,D+1,S,F,result)
        elif nbF > F:
            nbPerson -= 3
            result.append(resDisponibleF[F])
            return tmp(nbPerson,D,S,F+1,result)
        elif nbS > S:
            nbPerson -= 1
            result.append(resDisponibleS[S])
            return tmp(nbPerson,D,S+1,F,result)
        else:
            return []


    print('nbPerson:',nbPerson)
    return tmp(nbPerson,0,0,0,[])


def accepterDemande(request):
    if request.session.get("username") != "root":
        infoType = 'warning'
        info = "Reconnectez s'il vous plait"
        return render(request, "index.html", {'info': info, 'infoType': infoType})

    if request.method == "GET":
        id = request.GET['id']
        demande = Demande.objects.get(id=id)
        info = "il n y a plus ressource disponible"
        infoType = "warning"
        if demande.status == "attendu":
            demandePlans = DemandePlan.objects.filter(demande=demande)
            planId = demandePlans[0].plan.id
            plan = Plan.objects.get(id=planId)
            res = chercherRes(request, plan)
            print('res:',res)
            for i in res:
                info = "Felicitation !"
                infoType = "success"
                PlanRessource.objects.create(plan = plan,ressource=i)
                plan.status = "accepte"
                plan.save()
                demande.status = "accepte"
                demande.save()
        else:
            info = "Cette demande est deja acceptee"
            infoType = 'danger'
        demandes = Demande.objects.all()
        return render(request,'listDemandes.html',{'info':info,'infoType':infoType,'demandes':demandes,'flag':'1'})

    return redirect('/gestionnaire/listDemandes/?flag=1')

