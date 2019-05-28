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


class Plan(models.Model):
    numero = models.IntegerField(default=1)
    createTime = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    checkin = models.DateField()
    checkout = models.DateField()
    nbPerson = models.IntegerField(default=2)
    status = models.CharField(max_length=20, default="attendu")
    owner = models.ForeignKey(Client,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="attendu")

class Demande(models.Model):
    numero = models.IntegerField(default=1)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,default=None)
    createTime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, default="attendu")

class DemandePlan(models.Model):
    demande = models.ForeignKey(Demande,on_delete=models.CASCADE,default=None)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,default=None)
