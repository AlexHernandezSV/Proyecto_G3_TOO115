from email import message, message_from_file
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import Aspirante, JefeOperaciones
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def holamundo(request):
    return render(request,'gestionAsociados/holamundo.html')

"""def crearUsuario(request):

    return render(request, 'gestionAsociados/singUp.html')"""

class Register(View):
    def get(self,request):
        form = registerAspirantForm()
        return render(request, "gestionAsociados/singUp.html",{"form":form})

    def post(self, request):
        form = registerAspirantForm(request.POST)
        if form.is_valid():
            nombre = form.__getitem__('nombre').value()
            apellido = form.__getitem__('apellido').value()
            email = form.__getitem__('email').value()
            contra = get_random_string(length=8)
            print(contra)
            usuario = Aspirante.objects.create_user(email,email,contra)
            usuario.first_name = nombre
            usuario.last_name = apellido
            usuario.save()
            print(contra)
            mensaje = 'usuario: '+ email+' Contraseña: '+contra
            print(mensaje)
            send_mail(
                'Cooperativa Credenciales de usuario',
                mensaje,
                '',
                [email],
                fail_silently=False,
            )
            return redirect('/holamundo')
        else:
            pass

#view para logear
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('holamundo')
            else:
                message.error(request,"Usuario no registrado en el sistema")
        else:
            message.error(request,"Informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "gestionAsociados/login.html",{"form":form})
