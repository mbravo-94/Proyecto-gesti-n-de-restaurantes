from django.contrib import admin
from .models import Menu, Mesa, Empleado, Venta

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'puesto', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido')

admin.site.register(Menu)
admin.site.register(Mesa)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Venta)
