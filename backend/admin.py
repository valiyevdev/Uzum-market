from django.contrib import admin
from .models import Narsalar, Caruselimg  # ✅ IKKALA modelni import qildik

admin.site.register(Narsalar)
admin.site.register(Caruselimg)
