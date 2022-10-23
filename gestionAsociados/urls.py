from django.urls import include,path
import user
from . import views
from .views import crearPeticionAdmision, login_user
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', views.home),
    path('holamundo', views.holamundo),
    path('register', views.Register.as_view()),
    path('registerJO', views.RegisterJefeOperaciones.as_view()),
    path('registerCJ', views.RegisterCajero.as_view()),
    path('login', login_user,name="iniciar sesion"),
    path('user/', include('user.urls')),
    path('solicitud_aspirante', crearPeticionAdmision)    
]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
