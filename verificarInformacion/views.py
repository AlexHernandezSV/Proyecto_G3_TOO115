from pydoc import Doc
from django.shortcuts import render, redirect
from .forms import getId
from django.contrib import messages
from django.contrib.auth import login
from gestionAsociados.models import PeticionAdmision, Pais, DocIdentidad, Negocio, Trabajo, Vivienda, Conyuge, Beneficiario, Familiar, ReferenciaPersonal, Asociacion, DocAnexo, ReciboIngreso, Cuenta, TipoDocIdentidad, Departamento, Municipio
from gestionCooperativa.models import DatosCoop

# Create your views here.

def verInfoAsociado(request, id):
    print(id)
    #mostrar datos
    #aspirante = PeticionAdmision.objects.filter(id = id)

    #acceso a modelos
    peticionAdmision= PeticionAdmision.objects.all()
    pais= Pais.objects.all()
    docIdentidad= DocIdentidad.objects.all()
    negocio= Negocio.objects.all()
    trabajo= Trabajo.objects.all()
    vivienda= Vivienda.objects.all()
    conyuge= Conyuge.objects.all()
    beneficiario= Beneficiario.objects.all()
    familiar= Familiar.objects.all()
    referenciaPersonal= ReferenciaPersonal.objects.all()
    asociacion = Asociacion.objects.all()
    docAnexo = DocAnexo.objects.all()
    reciboIngreso = ReciboIngreso.objects.all()
    cuenta = Cuenta.objects.all()
    tipoDocIdentidad=TipoDocIdentidad.objects.all()
    departamento=Departamento.objects.all()
    municipio=Municipio.objects.all()
    empresa = DatosCoop.objects.all()

    #form de label de id
    form = getId(id)

    
    if request.method == "POST":
        if "aprobar" in request.POST:
            ins = PeticionAdmision.objects.get(id=id)
            ins.verificada = request.POST["aprobar"]
            ins.save(update_fields=['verificada'])

            ins.observacionesVerificado = request.POST["observaciones"]
            ins.save(update_fields=['observacionesVerificado'])

            ins.ejecutivoVerificado = request.POST["nombreE"]
            ins.save(update_fields=['ejecutivoVerificado'])
            messages.success(request, "Aspirante Verificado")
        if "denegar" in request.POST:
            ins = PeticionAdmision.objects.get(id=id)
            ins.verificada = request.POST["denegar"]
            ins.save(update_fields=['verificada'])

            ins.observacionesVerificado = request.POST["observaciones"]
            ins.save(update_fields=['observacionesVerificado'])

            ins.ejecutivoVerificado = request.POST["nombreE"]
            ins.save(update_fields=['ejecutivoVerificado'])
            messages.success(request, "Aspirante no Verificado")

        

        return redirect("/verListaAsociado")
    
    return render(request,'verificarInformacion/verInfoAsociado.html',
    {
        #forms
        "form":form,
    
        #modelos
        "peticionAdmision":peticionAdmision,
        "pais":pais,
        "docIdentidad": docIdentidad,
        "negocio":negocio,
        "trabajo":trabajo,
        "vivienda":vivienda,
        "conyuge":conyuge,
        "beneficiario":beneficiario,
        "familiar":familiar,
        "referenciaPersonal":referenciaPersonal,
        "asociacion":asociacion,
        "docAnexo":docAnexo,
        "reciboIngreso":reciboIngreso,
        "cuenta":cuenta,
        "tipoDocIdentidad":tipoDocIdentidad,
        "departamento":departamento,
        "municipio":municipio,
        'thisCoop':empresa,

        #id
        "var":id
    })
    

def verListaAsociado(request):
    #mostrar datos
    #mostrar= DatosCoop.objects.all()
    mostrar= PeticionAdmision.objects.all()

    #return render(request,'gestionCooperativa/verInfoCoop.html', {'mostrar':mostrar})
    return render(request,'verificarInformacion/verListaAsociado.html', {'mostrar':mostrar})
 

def editarInfoAsociado(request, id):
    print(id)
    #mostrar datos
    #aspirante = PeticionAdmision.objects.filter(id = id)

    #acceso a modelos
    peticionAdmision= PeticionAdmision.objects.all()
    pais= Pais.objects.all()
    docIdentidad= DocIdentidad.objects.all()
    negocio= Negocio.objects.all()
    trabajo= Trabajo.objects.all()
    vivienda= Vivienda.objects.all()
    conyuge= Conyuge.objects.all()
    beneficiario= Beneficiario.objects.all()
    familiar= Familiar.objects.all()
    referenciaPersonal= ReferenciaPersonal.objects.all()
    asociacion = Asociacion.objects.all()
    docAnexo = DocAnexo.objects.all()
    reciboIngreso = ReciboIngreso.objects.all()
    cuenta = Cuenta.objects.all()
    tipoDocIdentidad=TipoDocIdentidad.objects.all()
    departamento=Departamento.objects.all()
    municipio=Municipio.objects.all()
    empresa = DatosCoop.objects.all()

    #form de label de id
    form = getId(id)

    
    if request.method == "POST":
        ins = PeticionAdmision.objects.get(id=id)
        ins.nombre1 = request.POST["nombre1"]
        ins.nombre2 = request.POST["nombre2"]
        ins.nombre3 = request.POST["nombre3"]
        ins.apellido1 = request.POST["apellido1"]
        ins.apellido2 = request.POST["apellido2"]
        #ins.fechaNac = request.POST["fechaNac"]
        ins.lugarNac = request.POST["lugarNac"]
        ins.direccion = request.POST["direccion"]
        ins.email = request.POST["email"]
        ins.departamento_id = request.POST["departamentoId"]
        ins.municipio_id = request.POST["municipioId"]
        ins.pais_id = request.POST["paisId"]
        ins.personasDependientes = request.POST["personasDependientes"]
        
        ins.save(update_fields=['nombre1', 'nombre2', 'nombre3', 'apellido1', 'apellido2', "lugarNac", 'direccion', 'email', 'departamento_id', 'municipio_id', 'pais_id', 'personasDependientes'])

        doc = DocIdentidad.objects.get(id=id)
        doc.tipoDoc_id = request.POST["tipoDoc_id"]
        doc.numero = request.POST["numeroDoc"]
        doc.save(update_fields=['tipoDoc_id', 'numero'])

        viv = Vivienda.objects.get(id=id)
        viv.propietario = request.POST["propietario"]
        viv.parentesco = request.POST["parentesco"]
        viv.tenenciaVivienda = request.POST["tenenciaVivienda"]
        viv.tiempo = request.POST["tiempo"]
        viv.save(update_fields=['propietario', 'parentesco', 'tenenciaVivienda', 'tiempo'])

        trab= Trabajo.objects.get(id=id)
        trab.tipo = request.POST["tipo"]
        trab.lugarTrabajo = request.POST["lugarTrabajo"]
        trab.direccion = request.POST["direccionT"]
        trab.telefono = request.POST["telefonoT"]
        trab.email = request.POST["emailTrabajo"]
        trab.sueldo = request.POST["sueldoTrabajo"]
        trab.cargo = request.POST["cargoT"]
        trab.jefe = request.POST["jefeT"]
        trab.save(update_fields=['tipo', 'lugarTrabajo', 'direccion', 'telefono', 'email', 'sueldo', 'cargo', 'jefe'])

        
        
        #neg= Negocio.objects.get(id=id)
        #neg.nombreNegocio = request.POST["NombreNegocio"]
        #neg.direccion = request.POST["direccionNegocio"]
        #neg.telefono = request.POST["telefonoNegocio"]
        #neg.email = request.POST["emailnegocio"]
        #neg.numRegistroIva = request.POST["numRegistro"]
        #neg.giro = request.POST["giroNegocio"]
        #neg.numTrabajadores = request.POST["trabajadoresNegocio"]
        #neg.capital = request.POST["capitalNegocio"]
        #neg.mercancia = request.POST["mercanciaNegocio"]
        #neg.mobiliarioEquipo = request.POST["mobiliarioNegocio"]
        #neg.save(update_fields=['nombreNegocio', 'direccion', 'telefono', 'email', 'numRegistroIva', 'giro', 'numTrabajadores', 'capital', 'mercancia', 'mobiliarioEquipo'])


        con=Conyuge.objects.get(id=id)
        con.nombre=request.POST["nombreC"]
        con.apellido=request.POST["apellidoC"]
        con.docIdentidad=request.POST["docC"]
        con.telefono=request.POST["telefonoC"]
        con.save(update_fields=['nombre', 'apellido', 'docIdentidad', 'telefono'])

        fam=Familiar.objects.get(id=id)
        fam.parentesco=request.POST['parentescoF']
        fam.nombre=request.POST['nombreF']
        fam.apellido=request.POST['apellidoF']
        fam.telefono=request.POST['telefonoF']
        fam.email=request.POST['emailF']
        fam.departamento_id=request.POST['DepartamentoF']
        fam.municipio_id=request.POST['municipioF']
        fam.save(update_fields=['parentesco', 'nombre', 'apellido', 'telefono', 'email', 'departamento_id', 'municipio_id'])

        ref=ReferenciaPersonal.objects.get(id=id)
        ref.nombre=request.POST["nombreR"]
        ref.apellido=request.POST["apellidoR"]
        ref.telefono=request.POST["telefonoR"]
        ref.email=request.POST["emailR"]
        ref.save(update_fields=['nombre', 'apellido', 'telefono', 'email'])

        ben=Beneficiario.objects.get(id=id)
        ben.parentesco=request.POST["parentescoB"]
        ben.nombre=request.POST["nombreB"]
        ben.apellido=request.POST["apellidoB"]
        ben.beneficio=request.POST["beneficioB"]
        ben.save(update_fields=['parentesco', 'nombre', 'apellido', 'beneficio'])








        

        
        messages.success(request, "Aspirante Verificado")
        return redirect("/home")
    
    return render(request,'verificarInformacion/editarInfoAsociado.html',
    {
        #forms
        "form":form,
    
        #modelos
        "peticionAdmision":peticionAdmision,
        "pais":pais,
        "docIdentidad": docIdentidad,
        "negocio":negocio,
        "trabajo":trabajo,
        "vivienda":vivienda,
        "conyuge":conyuge,
        "beneficiario":beneficiario,
        "familiar":familiar,
        "referenciaPersonal":referenciaPersonal,
        "asociacion":asociacion,
        "docAnexo":docAnexo,
        "reciboIngreso":reciboIngreso,
        "cuenta":cuenta,
        "tipoDocIdentidad":tipoDocIdentidad,
        "departamento":departamento,
        "municipio":municipio,
        'thisCoop':empresa,

        #id
        "var":id
    })