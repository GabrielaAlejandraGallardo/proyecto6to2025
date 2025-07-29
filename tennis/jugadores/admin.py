
from django.contrib import admin
from .models import *
from .models import Deporte,Talla# Register your models here.

admin.site.register(Jugador)
admin.site.register(Deporte)
admin.site.register(Talla)


