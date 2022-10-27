from cmath import inf
from email import message, message_from_file
from pyexpat.errors import messages
from queue import Empty
from sys import prefix
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
        formVivienda = ViviendaForm(request.POST)
        formFamiliar = FamiliaresForm(request.POST)
        formFamiliar2 = FamiliaresForm(request.POST,prefix='2')
        formConyuge = ConyegeForm(request.POST)
        formTrabajo = TrabajoForm(request.POST)
        formNegocio = NegocioForm(request.POST)
        formRefPersonal = ReferenciaPersonalForm(request.POST)
        formRefPersonal2 = ReferenciaPersonalForm(request.POST,prefix='2')
        formBeneficiario = BeneficiarioFormSet(request.POST,request.FILES)
        formDocAnexo = DocAnexoForm(request.POST,request.FILES,prefix='doc1')
        formDocAnexo2 = DocAnexoForm(request.POST,request.FILES,prefix='doc2')
        formDocAnexo3= DocAnexoForm(request.POST,request.FILES,prefix='doc3')
        print('antes del if')
        #arregloFormularios = [formPeticion,formVivienda,formFamiliar,formFamiliar2,formBeneficiario,formRefPersonal2,formConyuge,formTrabajo,formNegocio,formRefPersonal]
        if (formDocAnexo.is_valid() and formDocAnexo2.is_valid() and formDocAnexo3.is_valid() and formPeticion.is_valid() and formFamiliar.is_valid() and formFamiliar2.is_valid() and formBeneficiario.is_valid() and formConyuge.is_valid() and formTrabajo.is_valid() and formNegocio.is_valid() and formRefPersonal.is_valid() and formRefPersonal2.is_valid() and formVivienda.is_valid()):
        #if(validarFormularios(arregloFormularios)):  
            print('Despues de if') 
            infFormPeticion = formPeticion.cleaned_data
            infFormVivienda = formVivienda.cleaned_data
            infFormFamilar= formFamiliar.cleaned_data
            infFormFamiliar2 = formFamiliar2.cleaned_data
            infFormConyuge = formConyuge.cleaned_data
            infFormTrabajo = formTrabajo.cleaned_data
            infFomrNegocio = formNegocio.cleaned_data
            infFormRefPersonal = formRefPersonal.cleaned_data
            infFormRefPersonal2 = formRefPersonal2.cleaned_data
            infFormDocAnexo = formDocAnexo.cleaned_data
            infFormDocAnexo2 = formDocAnexo2.cleaned_data
            infFormDocAnexo3 = formDocAnexo3.cleaned_data

            miPeticion = PeticionAdmision(
                nombre1 = infFormPeticion["nombre1"], 
                nombre2 = infFormPeticion["nombre2"],
                nombre3 = infFormPeticion["nombre3"],
                apellido1 = infFormPeticion["apellido1"],
                apellido2 = infFormPeticion["apellido2"],
                fechaNac =infFormPeticion["fechaNac"],
                lugarNac = infFormPeticion["lugarNac"],
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
             
            try:

                miPeticion.save()

                for beneficiario in formBeneficiario:
                    infBeneficiario = beneficiario.cleaned_data

                    beneficiarioObject = Beneficiario(
                        parentesco = infBeneficiario["parentesco"],
                        nombre = infBeneficiario["nombre"],
                        apellido = infBeneficiario["apellido"],
                        beneficio = infBeneficiario["beneficio"],
                        peticionAdmision = miPeticion,
                    )
                    beneficiarioObject.save()

                vivienda = Vivienda(
                    propietario = infFormVivienda['propietario'],
                    parentesco = infFormVivienda['parentesco'],
                    tenenciaVivienda = infFormVivienda['tenenciaVivienda'],
                    tiempo = infFormVivienda['tiempo'],
                    ubicacion = infFormVivienda['ubicacion'],
                    peticionAdmision = miPeticion
                )
                documentoIdentificacion = DocIdentidad(
                    tipoDoc = infFormPeticion['tipoDoc'],
                    numero = infFormPeticion['numeroDoc'],
                    peticionAdmision = miPeticion
                )

                conyuge = Conyuge(
                    nombre = infFormConyuge["nombreC"],
                    apellido = infFormConyuge["apellidoC"],
                    docIdentidad = infFormConyuge["docIdentidadC"],
                    telefono= infFormConyuge["telefonoC"],
                    peticionAdmision = miPeticion,
                )
                if((infFormTrabajo['tipo']!='')):
                    trabajo = Trabajo(
                        tipo =  infFormTrabajo["tipo"],
                        lugarTrabajo = infFormTrabajo["lugarTrabajo"],
                        direccion =  infFormTrabajo["direccionTrabajo"],
                        telefono =  infFormTrabajo["telefonoTrabajo"],
                        email =  infFormTrabajo["emailTrabajo"],
                        sueldo =  infFormTrabajo["sueldo"],
                        cargo = infFormTrabajo["cargo"],
                        jefe = infFormTrabajo["jefe"],
                        peticionAdmision = miPeticion  
                    )
                    trabajo.save()

                print('hola')

                if(infFomrNegocio['nombreNegocio']!=''):
                    print('hola2')
                    negocio = Negocio(
                        nombreNegocio = infFomrNegocio["nombreNegocio"],
                        direccion = infFomrNegocio["direccionNegocio"],
                        telefono = infFomrNegocio["telefonoNegocio"],
                        email = infFomrNegocio["emailNegocio"],
                        numRegistroIva = infFomrNegocio["numRegistroIva"],
                        giro = infFomrNegocio["giro"],
                        numTrabajadores = infFomrNegocio["numTrabajadores"],
                        capital = infFomrNegocio["capital"],
                        mercancia = infFomrNegocio["mercancia"],
                        mobiliarioEquipo = infFomrNegocio["mobiliarioEquipo"],
                        peticionAdmision = miPeticion
                    )
                    negocio.save()

                print('hola3')
                refPersonal = ReferenciaPersonal(
                    nombre = infFormRefPersonal["nombreRef"],
                    apellido = infFormRefPersonal["apellidoRef"],
                    telefono = infFormRefPersonal["telefonoRef"],
                    email = infFormRefPersonal["emailRef"],
                    peticionAdmision = miPeticion
                )
                refPersonal2 = ReferenciaPersonal(
                    nombre = infFormRefPersonal2["nombreRef"],
                    apellido = infFormRefPersonal2["apellidoRef"],
                    telefono = infFormRefPersonal2["telefonoRef"],
                    email = infFormRefPersonal2["emailRef"],
                    peticionAdmision = miPeticion
                )
                refFamiliar = Familiar(
                    parentesco = infFormFamilar["parentescoFamiliar"],
                    nombre = infFormFamilar["nombreFamiliar"],
                    apellido = infFormFamilar["apellidoFamiliar"],
                    telefono = infFormFamilar["telefonoFamiliar"],
                    email = infFormFamilar["emailFamiliar"],
                    municipio= infFormFamilar["municipioFamiliar"],
                    departamento= infFormFamilar["departamentoFamiliar"],
                    peticionAdmision = miPeticion
                )
                refFamiliar2 = Familiar(
                    parentesco = infFormFamiliar2["parentescoFamiliar"],
                    nombre = infFormFamiliar2["nombreFamiliar"],
                    apellido = infFormFamiliar2["apellidoFamiliar"],
                    telefono = infFormFamiliar2["telefonoFamiliar"],
                    email = infFormFamiliar2["emailFamiliar"],
                    municipio= infFormFamiliar2["municipioFamiliar"],
                    departamento= infFormFamiliar2["departamentoFamiliar"],
                    peticionAdmision = miPeticion
                )
                docAnexo1 = DocAnexo(
                    nombre = infFormDocAnexo['nombreDocAnexo'],
                    doc = infFormDocAnexo['docAnexo'],
                    peticionAdmision = miPeticion
                )

                docAnexo2 = DocAnexo(
                    nombre = infFormDocAnexo2['nombreDocAnexo'],
                    doc = infFormDocAnexo2['docAnexo'],
                    peticionAdmision = miPeticion
                )

                docAnexo3 = DocAnexo(
                    nombre = infFormDocAnexo3['nombreDocAnexo'],
                    doc = infFormDocAnexo3['docAnexo'],
                    peticionAdmision = miPeticion
                )

                print('hola4')

                documentoIdentificacion.save()
                vivienda.save()
                conyuge.save()
                refPersonal.save()
                refPersonal2.save()
                refFamiliar.save()
                refFamiliar2.save()
                docAnexo1.save()
                docAnexo2.save()
                docAnexo3.save()
                print('hola5')
                return redirect('/solicitud_aspirante')
            except:
                print('Error al procesar la peticion')
                
    else:
        formPeticion = peticionAspiranteForm()
        formVivienda = ViviendaForm()
        formFamiliar = FamiliaresForm()
        formFamiliar2 = FamiliaresForm(prefix='2')
        formBeneficiario = BeneficiarioFormSet(queryset=Beneficiario.objects.none())
        formConyuge = ConyegeForm()
        formTrabajo = TrabajoForm()
        formNegocio = NegocioForm()
        formRefPersonal = ReferenciaPersonalForm()
        formRefPersonal2 = ReferenciaPersonalForm(prefix='2')
        formDocAnexo = DocAnexoForm(prefix='doc1')
        formDocAnexo2 = DocAnexoForm(prefix='doc2')
        formDocAnexo3 = DocAnexoForm(prefix='doc3')
    return render(
        request,'gestionAsociados/solicitudAdmision.html',
        {
            "formPeticion":formPeticion,
            "formFamiliar":formFamiliar,
            "formFamiliar2":formFamiliar2,
            "formBeneficiario":formBeneficiario,
            "formConyuge":formConyuge,
            "formTrabajo":formTrabajo,
            "formNegocio":formNegocio,
            "formRefPersonal":formRefPersonal,
            "formRefPersonal2":formRefPersonal2,
            "formVivienda":formVivienda,
            "formDocAnexo":formDocAnexo,
            "formDocAnexo2":formDocAnexo2,
            "formDocAnexo3":formDocAnexo3
        })

def validarFormularios(formularios):
    for formulario in formularios:
        if formulario.is_valid():
            control = True
        else: 
            control = False
            return control
    return control
