from django.contrib import admin
from .models import Cliente, TipoHabitacion, Habitacion, Reservacion

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'email',)

class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'cantidad_camas', 'tarifa',)

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cantidad_personas', 'check_in', 'check_out',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Reservacion, ReservacionAdmin)
