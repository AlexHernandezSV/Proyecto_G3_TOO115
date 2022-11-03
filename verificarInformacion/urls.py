from django import views
from django.urls import include, path
from . import views


urlpatterns = [
    
    path("verInfoAsociado/<id>/", views.verInfoAsociado, name = 'id'),
    path('verListaAsociado', views.verListaAsociado),

]