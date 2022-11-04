from django import views
from django.urls import include, path
from . import views
from .views import *


urlpatterns = [
    path('Cuotas', views.tableCuotas , name="Tabla Cuotas"),
    path('registrarCuota', views.RegistrarCuotas, name='Registrar Cuota'),
    path('eliminarCuota/<int:id>', views.EliminarCuotas,name="Eliminar Cuotas"),
    path('cancelar_recibo/<int:id>', cancelarReciboIngreso),
    path('gestionar_recibos',listaRecibos)

]