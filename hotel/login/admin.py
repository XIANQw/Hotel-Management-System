from django.contrib import admin
from login.models import *

# Register your models here.
class clientAdmin(admin.ModelAdmin):
    list_display = ('login', 'nom', 'prenom', 'adresse','tel')  # list

admin.site.register(Client,clientAdmin)

