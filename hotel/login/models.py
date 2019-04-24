from django.db import models

# Create your models here.

class Client(models.Model):
    login = models.CharField(max_length=32,default='defaut')
    pwd = models.CharField(max_length=20,default='defaut')
    nom = models.CharField(max_length=32,default='defaut')
    prenom = models.CharField(max_length=32,default='defaut')
    email = models.EmailField(max_length= 32,default='defaut')
    adresse = models.CharField(max_length=32,null=True,blank=True)
    tel = models.CharField(max_length=32,null=True,blank=True)


class Demande(models.Model):
    demandeDate = models.DateField(auto_now_add=True)
    checkin = models.DateField(auto_now_add=True)
    checkout = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default="attendu")
    client = models.ForeignKey(Client,on_delete=models.CASCADE)



class Ressource(models.Model):
    nom_ressource= models.CharField(max_length=32, default="default")
    price = models.IntegerField(default=0)
    type=models.CharField(max_length=32,default="default")
    status = models.CharField(max_length=32,default="attendu")
    taille = models.IntegerField(default=0)
    demande = models.ForeignKey(Demande,on_delete=models.CASCADE)