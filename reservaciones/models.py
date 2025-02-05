from django.db import models
from django.core.validators import EmailValidator
from .validators import validar_numero, validar_texto

# Create your models here.
class Cliente(models.Model):
    nombres = models.CharField(max_length=180, validators=[validar_texto,])
    apellidos = models.CharField(max_length=180, validators=[validar_texto,])
    email = models.CharField(max_length=180, unique=True, validators=[EmailValidator('No es una dirección de email valida'),])
    def __str__(self) -> str:
        return self.nombres+' '+self.apellidos

class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=180, unique=True, validators=[validar_texto,])
    cantidad_camas = models.PositiveIntegerField()
    tarifa = models.FloatField(validators=[validar_numero,])
    def __str__(self) -> str:
        return self.nombre

class Habitacion(models.Model):
    nombre = models.CharField(max_length=180, unique=True, validators=[validar_texto,])
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre
    
class Reservacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitaciones = models.ManyToManyField(Habitacion)
    cantidad_personas = models.PositiveIntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    def __str__(self) -> str:
        return self.check_in+' - '+self.check_out
