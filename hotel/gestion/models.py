from login.models import *
# Create your models here.
class Meuble(models.Model):
    nom_Meuble =  models.CharField(max_length=32, default="default")
    status = models.CharField(max_length=20, default="bon")

class Ressource(models.Model):
    numero = models.CharField(max_length=32, default="default")
    prix = models.IntegerField(default=0)
    type = models.CharField(max_length=32,default="default")
    taille = models.IntegerField(default=0)
    def __unicode__(self):
        return self.numero

class Concerne_Meuble(models.Model):
    ressource = models.ForeignKey(Ressource, default = None, on_delete=models.CASCADE)
    meuble = models.ForeignKey(Meuble, default = None, on_delete=models.CASCADE)


class Demande(models.Model):
    demandeTime = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    checkin = models.DateField()
    checkout = models.DateField()
    nbPerson = models.IntegerField(default=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="attendu")