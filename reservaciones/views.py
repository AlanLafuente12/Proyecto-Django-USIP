from django.shortcuts import render
from .models import Reservacion, Habitacion, TipoHabitacion, Cliente
from rest_framework import viewsets, generics
from .serializers import ReservacionSerializer, HabitacionSerializer, TipoHabitacionSerializer, ClienteSerializer

# Create your views here.
# Model View Set
class ReservacionViewSet(viewsets.ModelViewSet):
	queryset = Reservacion.objects.all()
	serializer_class = ReservacionSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
	queryset = Habitacion.objects.all()
	serializer_class = HabitacionSerializer

class TipoHabitacionViewSet(viewsets.ModelViewSet):
	queryset = TipoHabitacion.objects.all()
	serializer_class = TipoHabitacionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	
# Generic API view
class ClienteCreateView(generics.CreateAPIView, generics.ListAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer