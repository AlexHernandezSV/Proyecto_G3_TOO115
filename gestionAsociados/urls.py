from django.urls import include,path

import user
from . import views
from .views import login_user

urlpatterns = [
    path('holamundo', views.holamundo),
    path('register', views.Register.as_view()),
    path('registerJO', views.RegisterJefeOperaciones.as_view()),
    path('registerCJ', views.RegisterCajero.as_view()),
    path('login', login_user,name="iniciar sesion"),
    path('user/', include('user.urls')),
]