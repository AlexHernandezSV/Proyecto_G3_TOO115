from django.urls import include,path
from . import views
from .views import login_user

urlpatterns = [
    path('holamundo', views.holamundo),
    path('register', views.Register.as_view()),
    path('login', login_user,name="iniciar sesion"),
]