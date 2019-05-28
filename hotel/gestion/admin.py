from django.contrib import admin

from gestion.models import *

# Register your models here.

class ressourceAdmin(admin.ModelAdmin):
    list_display = ('numero', 'prix', 'type')  # list

class planAdmin(admin.ModelAdmin):
    list_display = ('id', 'checkin', 'checkout','nbPerson', 'owner','status')  # list

class demandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client','status')  # list

class demandePlanAdmin(admin.ModelAdmin):
    list_display = ('id','demande','plan')

class MeubleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_Meuble','status')  # list

class Concerne_MeubleAdmin(admin.ModelAdmin):
    list_display = ('id', 'ressource', 'meuble')  # list

admin.site.register(Ressource,ressourceAdmin)
admin.site.register(Demande,demandeAdmin)
admin.site.register(Meuble,MeubleAdmin)
admin.site.register(Concerne_Meuble,Concerne_MeubleAdmin)
admin.site.register(Plan,planAdmin)
admin.site.register(DemandePlan,demandePlanAdmin)
