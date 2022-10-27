from django import views
from django.urls import include, path
from . import views


urlpatterns = [
    
    path('Cuotas', views.tableCuotas , name="Tabla Cuotas"),
    path('registrarCuota', views.RegistrarCuotas, name='Registrar Cuota'),
    path('eliminarCuota/<int:id>', views.EliminarCuotas,name="Eliminar Cuotas"),

]