from django.contrib import admin

from App.models import Autos
from App.models import Motos
from App.models import Propietario
from App.models import Mensajeria
# Register your models here.

admin.site.register(Autos)

admin.site.register(Motos)

admin.site.register(Propietario)

admin.site.register(Mensajeria)