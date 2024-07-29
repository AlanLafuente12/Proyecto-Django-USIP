from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename="clientes")
router.register(r'habitaciones', views.HabitacionViewSet, basename="habitaciones")
router.register(r'tiposhabitacion', views.TipoHabitacionViewSet, basename="tiposhabitacion")
router.register(r'reservaciones', views.ReservacionViewSet, basename="reservaciones")

urlpatterns = [
    path('', include(router.urls)),
]