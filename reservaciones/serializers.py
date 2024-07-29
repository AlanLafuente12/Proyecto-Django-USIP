from rest_framework import serializers
from .models import Reservacion, Habitacion, TipoHabitacion, Cliente

# Transforma el objeto python del orm a formato json
class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
