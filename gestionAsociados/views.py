from pyexpat.errors import messages
from email import message, message_from_file
from re import L
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import date,datetime
from user.models import Aspirante, Cajero, Ejecutivo, JefeOperaciones
from gestionCooperativa.models import DatosCoop
from cobros.models import Cuota
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from gestionAsociados.models import PeticionAdmision
from user.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
def holamundo(request):
    return render(request,'gestionAsociados/holamundo.html')

#pagina de inicio
def home(request):
    user = User.objects.all()
    empresa = DatosCoop.objects.all()
    peticionAdmision= PeticionAdmision.objects.all()

    currentUserName = request.user.get_username()
    print(currentUserName)

    currentUserId = request.user.id
    print(currentUserId)
    existe = False

    if peticionAdmision.filter(id=currentUserId).exists():
        existe = True
        
    
    print(existe)

    


    
    return render(request,'gestionAsociados/index.html',
    {
        'thisCoop':empresa,
        "peticionAdmision":peticionAdmision,
        #existencia
        "existe":existe
    })

def cerrarSesion(request):
    logout(request)
    return redirect('/home')

def homeEjecutiva(request):
    return render(request,'gestionAsociados/homeEjecutiva.html')
"""def crearUsuario(request):

    return render(request, 'gestionAsociados/singUp.html')"""

class Register(View):
    
    def get(self,request):
        empresa = DatosCoop.objects.all()
        form = registerAspirantForm()
        return render(request, "gestionAsociados/singUp.html",{"form":form,'thisCoop':empresa})

    def post(self, request):
        form = registerAspirantForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            nombre = form.__getitem__('nombre').value()
            apellido = form.__getitem__('apellido').value()
            email = form.__getitem__('email').value()
            contra = get_random_string(length=8)
            try:
                usuario = Aspirante.objects.create_user(email,email,contra)
                usuario.first_name = nombre
                usuario.last_name = apellido
                
                print('hola1')
                usuario.save()
                mensaje = 'usuario: '+ email+' Contraseña: '+contra
                send_mail(
                    'Cooperativa Credenciales de usuario',
                    mensaje,
                    '',
                    [email],
                fail_silently=False,
            )
            except Exception as e:
                error  = e.__str__
                return render(request, "gestionAsociados/singUp.html",{"form":form,'error':error})
            return redirect('/holamundo')
        else:
            print(form.errors)
            return render(request, "gestionAsociados/singUp.html",{"form":form})




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
        empresa = DatosCoop.objects.all()
        form = registerAspirantForm()
        return render(request, "gestionAsociados/singUpCJ.html",{"form":form,'thisCoop':empresa})

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
            if usuario is not None:
                login(request,usuario)
                return redirect('/home')
            else:
                message.error(request,"Usuario no registrado en el sistema")
        else:
            message.error(request,"Informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "gestionAsociados/login.html",{"form":form})

def changePassword(request):
    try:
        empresa = DatosCoop.objects.all()
        aspirante = Aspirante.objects.get(id = request.user.id)
    except:
        pass
    if(request.method == 'POST'):
        formChangePassword = ChangePasswordForm(request.POST)
        if formChangePassword.is_valid():
            infFormChangePassword = formChangePassword.cleaned_data

            aspirante.set_password(infFormChangePassword['nueva'])
            
    else:

        formChangePassword = ChangePasswordForm()

    return render(request,'gestionAsociados/changePassword.html',{"formChangePassword":formChangePassword,'thisCoop':empresa})

@login_required
def crearPeticionAdmision(request):
    empresa = DatosCoop.objects.all()
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
                    #ubicacion = infFormVivienda['ubicacion'],
                    lat = infFormVivienda['lat'],
                    lng = infFormVivienda['lng'],
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
            "formDocAnexo3":formDocAnexo3,
            'thisCoop':empresa
        })

def miPerfil(request):
    if(request.method == 'POST'):
        #formFoto = FotoForm(request.POST,request.FILES)
        formFoto = FotoFormSet(request.POST,request.FILES)
        if formFoto.is_valid():
            infFormFoto = formFoto.cleaned_data
            #print(f.cleaned_data)
            #print(request.POST)
            #print(infFormFoto)
            foto = Foto(
                foto = infFormFoto["foto"],
                aspirante = request.user,
            )
            foto.save()
        return redirect('/mi_perfil')
    else:
        #formFoto = FotoForm()    
        formFoto = FotoFormSet()
        return render(request,"gestionAsociados/miPerfil.html",{'formFoto':formFoto})

def validarFormularios(formularios):
    for formulario in formularios:
        if formulario.is_valid():
            control = True
        else: 
            control = False
            return control
    return control

@login_required
def listAprobarPeticion(request):
    empresa = DatosCoop.objects.all()
    if request.user.role != 'JEFEOPERACIONES':
        return redirect('/home')
    else:
        peticiones = PeticionAdmision.objects.filter(estado = False,verificada= True)
        return render(request,'gestionAsociados/listaPeticionesVerificadas.html',{'peticiones':peticiones,'thisCoop':empresa})

def verSolicitudVerificada(request, id):
    if request.user.role != 'JEFEOPERACIONES':
        return redirect('/home')
    if(request.method == 'POST'):

        if('denegar' in request.POST):
            return redirect('/gestionar_peticiones_verificadas')
        if('aprobar') in request.POST:
            peticion = PeticionAdmision.objects.get(id=id)
            asociado = Aspirante.objects.get(id=peticion.aspirante.id)
            cuota = Cuota.objects.get(tipo=1)

            asociado.role = 'SOCIO'
            reciboIngreso = ReciboIngreso(
                monto = cuota.monto,
                descripcion = 'Pago por apertura de cuenta y expediente de asociado',
                tipo = 'Ingreso',
                aspirante = asociado,
                cancelado = False,
            )
            relleno = str(asociado.id)
            if(len(relleno)<5):
                relleno = relleno.zfill(5)
            codigoAsociado = peticion.apellido1[0].upper()+peticion.apellido2[0].upper()+ date.today().strftime("%y") +relleno
            print(codigoAsociado)

            cuenta = Cuenta(
                codigo = codigoAsociado,
                tipo = 'ahorro',
                saldo = 0,
                aspirante = asociado,
            )
            peticion.estado = True
            peticion.aprobada = True
            peticion.save()
            cuenta.save()
            reciboIngreso.save()
            asociado.save()

            mensaje = "Estimado(a). \n"+asociado.first_name+' '+asociado.last_name +' \n'
            mensaje += "Su solicitud ha sido aprobada por la Junta Directiva de la Cooperativa"
            mensaje += "\nCodigo de socio: " + cuenta.codigo
            email = asociado.email
            send_mail(
                'Resolución de solicitud',
                mensaje,
                '',
                [email],
                fail_silently=False,
            )
            
            return redirect('/gestionar_peticiones_verificadas')
            
    else:
        empresa = DatosCoop.objects.all()
        solicitud = PeticionAdmision.objects.get(id=id)
        conyuge = Conyuge.objects.get(peticionAdmision = solicitud)
        docIdentidad = DocIdentidad.objects.get(peticionAdmision = solicitud)
        vivienda = Vivienda.objects.get(peticionAdmision = id)
        negocio = ''
        trabajo = ''
        try:
            trabajo = Trabajo.objects.get(peticionAdmision= id)
            negocio = Negocio.objects.get(peticionAdmision= id)
        except:
            pass
        familiares = Familiar.objects.filter(peticionAdmision= id)
        referenciasPersonales = ReferenciaPersonal.objects.filter(peticionAdmision= id)
        beneficiarios = Beneficiario.objects.filter(peticionAdmision= id)
        docsAnexos = DocAnexo.objects.filter(peticionAdmision= id)
        departamento = Departamento.objects.all()
        municipio = Municipio.objects.all()

        return render(
            request,
            'gestionAsociados/verSolicitudVerificada.html',
            {
                'solicitud':solicitud,
                'con':conyuge,
                'docIdentidad':docIdentidad,
                'vivienda':vivienda,
                'trab':trabajo,
                'neg':negocio,
                'familiar':familiares,
                'referenciaPersonal':referenciasPersonales,
                'beneficiario':beneficiarios,
                'docAnexo':docsAnexos,
                'departamento':departamento,
                'municipio':municipio,
                'thisCoop':empresa
            })

def verCarnet(request):
    if (request.user.role != 'SOCIO'):
        return redirect('/home')
    else:
        cuenta = Cuenta.objects.get(aspirante = request.user.id)
        peticion = PeticionAdmision.objects.get(aspirante= request.user.id)
        empresa = DatosCoop.objects.get(id=1)
        foto = Foto.objects.get(aspirante = request.user)

        return render(request,'gestionAsociados/verCarnet.html',{'cuenta':cuenta,'peticion':peticion,'foto':foto,'empresa':empresa})



#registrar Ejecutivo
class RegisterEjecutivo(View):
    def get(self,request):
        empresa = DatosCoop.objects.all()
        form = registerAspirantForm()
        return render(request, "gestionAsociados/singUpEJ.html",{"form":form,'thisCoop':empresa})

    def post(self, request):
        form = registerAspirantForm(request.POST)
        if form.is_valid():
            nombre = form.__getitem__('nombre').value()
            apellido = form.__getitem__('apellido').value()
            email = form.__getitem__('email').value()
            contra = get_random_string(length=8)
            print(contra)
            usuario = Ejecutivo.objects.create_user(email,email,contra)
            usuario.first_name = nombre
            usuario.last_name = apellido
            usuario.save()
            print(contra)
            mensaje = 'usuario: '+ email+' Contraseña: '+contra
            print(mensaje)
            send_mail(
                'Cooperativa Credenciales de usuario ejecutivo',
                mensaje,
                '',
                [email],
                fail_silently=False,
            )
            return redirect('/holamundo')
        else:
            pass
