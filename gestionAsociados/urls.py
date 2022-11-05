from django.urls import include,path
import user
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from two_factor import views as tf_views


urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('', views.home),
    path('homeEjecutiva', views.homeEjecutiva),
    path('holamundo', views.holamundo),
    path('register', views.Register.as_view()),
    path('registerJO', views.RegisterJefeOperaciones.as_view()),
    path('registerCJ', views.RegisterCajero.as_view()),
    path('login', login_user,name="iniciar sesion"),
    #path('user/', include('user.urls')),
    path('solicitud_aspirante', crearPeticionAdmision),
    path('logout/',cerrarSesion),
    path('change_password',changePassword),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password_change',auth_views.PasswordChangeView.as_view(template_name='gestionAsociados/changePassword.html',success_url='/home')),
    #path('account/login', auth_views.LoginView.as_view(template_name='gestionAsociados/changePassword.html')),
    #path('accounts/login', auth_views.LoginView.as_view(template_name='gestionAsociados/changePassword.html')),
    path('mi_perfil',miPerfil),
    path('gestionar_peticiones_verificadas',listAprobarPeticion),
    path('ver_solicitud_verificada/<int:id>',verSolicitudVerificada),
    path('',include('verificarInformacion.urls')),
    path('registerEJ', views.RegisterEjecutivo.as_view()),
    path('carnet',verCarnet),
]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
