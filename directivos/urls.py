from django.urls import path
from . import views

urlpatterns = [
    path('addDirectivo/', views.addDirectivo, name="add-directivo"),
    path('listaDirec', views.Directivos, name="lista-directivos"),
    path('eliminarDirec/<int:id>', views.EliminarDirectivos , name="Eliminar Cuotas"),
]