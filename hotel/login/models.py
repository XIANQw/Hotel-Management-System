from django.db import models

# Create your models here.

class Gestionnaire(models.Model):
    login = models.CharField(max_length=32,default='defaut')
    pwd = models.CharField(max_length=20,default='defaut')


class Client(models.Model):
    login = models.CharField(max_length=32,default='defaut')
    pwd = models.CharField(max_length=20,default='defaut')
    nom = models.CharField(max_length=32,default='defaut')
    prenom = models.CharField(max_length=32,default='defaut')
    email = models.EmailField(max_length= 32,default='defaut')
    adresse = models.CharField(max_length=32,null=True,blank=True)
    tel = models.CharField(max_length=32,null=True,blank=True)
    def __unicode__(self):
        return self.login

