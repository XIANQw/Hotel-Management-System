from login.models import *
# Create your models here.

class Ressource(models.Model):
    numero = models.CharField(max_length=32, default="default")
    prix = models.IntegerField(default=0)
    type = models.CharField(max_length=32,default="default")
    taille = models.IntegerField(default=0)
    def __unicode__(self):
        return self.numero


class Demande(models.Model):
    demandeTime = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    checkin = models.DateField()
    checkout = models.DateField()
    nbPerson = models.IntegerField(default=2)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="attendu")