from django.contrib import admin
from login.models import Client
from gestion.models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Ressource)
admin.site.register(Demande)
