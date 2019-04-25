from django.db import models
from login.models import *
# Create your models here.
class Ressource(models.Model):
    numero = models.CharField(max_length=32, default="default")
    prix = models.IntegerField(default=0)
    type = models.CharField(max_length=32,default="default")
    taille = models.IntegerField(default=0)

class Demande(models.Model):
    demandeDate = models.DateField(auto_now_add=True)
    checkin = models.DateField(auto_now_add=True)
    checkout = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default="attendu")
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    demande = models.ManyToManyField(Ressource)