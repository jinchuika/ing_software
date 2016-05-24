from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.register(Tecnico)
admin.site.register(Cliente)
admin.site.register(TipoEquipo)
admin.site.register(Equipo)
admin.site.register(Garantia)
admin.site.register(TipoIncidencia)
admin.site.register(Incidencia)
admin.site.register(Factura)
admin.site.register(DetalleFactura)