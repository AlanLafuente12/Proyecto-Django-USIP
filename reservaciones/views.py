from django.shortcuts import render
from .models import Reservacion, Habitacion, TipoHabitacion, Cliente
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from .serializers import ReservacionSerializer, HabitacionSerializer, TipoHabitacionSerializer, ClienteSerializer, ReporteReservacionesSerializer

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
	
# Custom API view

@api_view(['GET'])
def reporte_reservaciones(request):
    """
    Reporte de reservaciones
    """

    try:
        reservaciones = Reservacion.objects.all()
        cantidad = reservaciones.count()
        return JsonResponse(
            ReporteReservacionesSerializer({
                "cantidad": cantidad,
                "reservaciones": reservaciones
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )
