from email import message, message_from_file
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import Aspirante, Cajero, JefeOperaciones
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
def holamundo(request):
    return render(request,'gestionAsociados/holamundo.html')

#pagina de inicio
def home(request):
    return render(request,'gestionAsociados/home.html')

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



#registrar jefe de operaciones
class RegisterJefeOperaciones(View):
    def get(self,request):
        form = registerAspirantForm()
        return render(request, "gestionAsociados/singUpJO.html",{"form":form})

    def post(self, request):
        form = registerAspirantForm(request.POST)
        if form.is_valid():
            nombre = form.__getitem__('nombre').value()
            apellido = form.__getitem__('apellido').value()
            email = form.__getitem__('email').value()
            contra = get_random_string(length=8)
            print(contra)
            usuario = JefeOperaciones.objects.create_user(email,email,contra)
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

#registrar Cajero
class RegisterCajero(View):
    def get(self,request):
        form = registerAspirantForm()
        return render(request, "gestionAsociados/singUpCJ.html",{"form":form})

    def post(self, request):
        form = registerAspirantForm(request.POST)
        if form.is_valid():
            nombre = form.__getitem__('nombre').value()
            apellido = form.__getitem__('apellido').value()
            email = form.__getitem__('email').value()
            contra = get_random_string(length=8)
            print(contra)
            usuario = Cajero.objects.create_user(email,email,contra)
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
def login_user(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(request,username=user_name, password=contra)
            print(usuario)
            if usuario is not None:
                login(request,usuario)
                return redirect('/holamundo')
            else:
                message.error(request,"Usuario no registrado en el sistema")
        else:
            message.error(request,"Informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "gestionAsociados/login.html",{"form":form})

@login_required
def crearPeticionAdmision(request):
    aspirante = Aspirante.objects.get(username=request.user)
    if request.method=="POST":
        formPeticion = peticionAspiranteForm(request.POST)
        formFamiliar = FamiliaresForm(request.POST)
        formBeneficiario = BeneficiarioForm(request.POST)
        formConyuge = ConyegeForm(request.POST)
        formTrabajo = TrabajoForm(request.POST)
        formNegocio = NegocioForm(request.POST)
        formRefPersonal = ReferenciaPersonalForm(request.POST)

        if formPeticion.is_valid() and formFamiliar.is_valid() and formBeneficiario.is_valid() and formConyuge.is_valid() and formTrabajo.is_valid() and formNegocio.is_valid() and formRefPersonal.is_valid():
            infFormPeticion = formPeticion.cleaned_data
            infFormFamilar= formFamiliar.cleaned_data
            infFormBeneficiario = formBeneficiario.cleaned_data
            infFormConyuge = formConyuge.cleaned_data
            infFormTrabajo = formTrabajo.cleaned_data
            infFomrNegocio = formNegocio.cleaned_data
            infFormRefPersonal = formRefPersonal.cleaned_data

            miPeticion = PeticionAdmision(
                nombre1 = infFormPeticion["nombre1"], 
                nombre2 = infFormPeticion["nombre2"],
                nombre3 = infFormPeticion["nombre3"],
                apellido1 = infFormPeticion["apellido1"],
                apellido2 = infFormPeticion["apellido2"],
                fechaNac =infFormPeticion["fechaNac"],
                direccion =infFormPeticion["direccion"],
                email = infFormPeticion["email"],
                personasDependientes = infFormPeticion["personasDependientes"],                                     
                #verificada = infFormPeticion["nombre1"],
                #aprobada = infFormPeticion["nombre1"],
                #estado = infFormPeticion["nombre1"],
                aspirante = aspirante,
                departamento = infFormPeticion["departamento"],
                municipio = infFormPeticion["municipio"],
                pais = infFormPeticion["pais"]
            )
            miPeticion.save()

            conyuge = Conyuge(
                nombre = infFormConyuge["nombre"],
                apellido = infFormConyuge["apellido"],
                docIdentidad = infFormConyuge["docIdentidad"],
                telefono= infFormConyuge["telefono"],
                peticionAdmision = miPeticion,
            )
            
            trabajo = Trabajo(
                tipo =  infFormTrabajo["tipo"],
                lugarTrabajo = infFormTrabajo["lugarTrabajo"],
                direccion =  infFormTrabajo["direccion"],
                telefono =  infFormTrabajo["telefono"],
                email =  infFormTrabajo["email"],
                sueldo =  infFormTrabajo["sueldo"],
                cargo = infFormTrabajo["cargo"],
                jefe = infFormTrabajo["jefe"],
                peticionAdmision = miPeticion  
            )
            negocio = Negocio(
                nombreNegocio = infFomrNegocio["nombreNegocio"],
                direccion = infFomrNegocio["direccion"],
                telefono = infFomrNegocio["telefono"],
                email = infFomrNegocio["email"],
                numRegistroIva = infFomrNegocio["numRegistroIva"],
                giro = infFomrNegocio["giro"],
                numTrabajadores = infFomrNegocio["numTrabajadores"],
                capital = infFomrNegocio["capital"],
                mercancia = infFomrNegocio["mercancia"],
                mobiliarioEquipo = infFomrNegocio["mobiliarioEquipo"],
                peticionAdmision = miPeticion
            )
            refPersonal = ReferenciaPersonal(
                nombre = infFormRefPersonal["nombre"],
                apellido = infFormRefPersonal["apellido"],
                telefono = infFormRefPersonal["telefono"],
                email = infFormRefPersonal["email"],
                peticionAdmision = miPeticion
            )
            refFamiliar = Familiar(
                parentesco = infFormFamilar["parentesco"],
                nombre = infFormFamilar["nombre"],
                apellido = infFormFamilar["apellido"],
                telefono = infFormFamilar["telefono"],
                email = infFormFamilar["email"],
                municipio= infFormFamilar["municipio"],
                departamento= infFormFamilar["departamento"],
                peticionAdmision = miPeticion
            )
            beneficiario = Beneficiario(
                parentesco = infFormBeneficiario["parentesco"],
                nombre = infFormBeneficiario["nombre"],
                apellido = infFormBeneficiario["apellido"],
                beneficio = infFormBeneficiario["beneficio"],
                peticionAdmision = miPeticion,
            )

            conyuge.save()
            trabajo.save()
            negocio.save()
            refPersonal.save()
            refFamiliar.save()
            beneficiario.save()
            

    else:
        formPeticion = peticionAspiranteForm()
        formFamiliar = FamiliaresForm()
        formBeneficiario = BeneficiarioForm()
        formConyuge = ConyegeForm()
        formTrabajo = TrabajoForm()
        formNegocio = NegocioForm()
        formRefPersonal = ReferenciaPersonalForm()
    return render(request,'gestionAsociados/crearPeticionAdmision.html',{"formPeticion":formPeticion,"formFamiliar":formFamiliar,"formBeneficiario":formBeneficiario,"formConyuge":formConyuge,"formTrabajo":formTrabajo,"formNegocio":formNegocio,"formRefPersonal":formRefPersonal})