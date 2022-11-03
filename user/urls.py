from django.urls import path
import user
from . import views

app_name = 'user'

urlpatterns = [
    #user
    #path('list/', lista, name ='user_list'),
    path('lista', views.lista , name="Lista usuarios"),

]