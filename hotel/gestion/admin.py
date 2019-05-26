from django.contrib import admin

from gestion.models import *

# Register your models here.

class ressourceAdmin(admin.ModelAdmin):
    list_display = ('numero', 'prix', 'type', 'taille')  # list

class demandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'checkin', 'checkout','nbPerson', 'client','status')  # list

admin.site.register(Ressource,ressourceAdmin)
admin.site.register(Demande,demandeAdmin)