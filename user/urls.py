from django.urls import path
import user
from user.views import *

app_name = 'user'

urlpatterns = [
    #user
    path('list/', lista, name ='user_list'),
]