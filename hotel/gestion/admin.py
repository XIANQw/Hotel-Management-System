from django.contrib import admin

from gestion.models import *

# Register your models here.

class ressourceAdmin(admin.ModelAdmin):
    list_display = ('numero', 'prix', 'type', 'taille')  # list

class planAdmin(admin.ModelAdmin):
    list_display = ('id', 'checkin', 'checkout','nbPerson', 'owner','status')  # list

class demandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client','status')  # list

class demandePlanAdmin(admin.ModelAdmin):
    list_display = ('id','demande','plan')

admin.site.register(Ressource,ressourceAdmin)
admin.site.register(Plan,planAdmin)
admin.site.register(Demande,demandeAdmin)
admin.site.register(DemandePlan,demandePlanAdmin)