from django.urls import include,path

import user
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('verInfoCoop', views.verInfoCoop),
    path('editarInfoCoop', views.editarInfoCoop),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

