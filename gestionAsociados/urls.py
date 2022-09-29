from django.urls import include,path
from . import views

urlpatterns = [
    path('holamundo', views.holamundo),
    path('register', views.Register.as_view())
]