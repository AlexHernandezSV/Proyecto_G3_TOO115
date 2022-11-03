from pydoc import Doc
from django.shortcuts import render, redirect
from .forms import getId
from django.contrib import messages
from django.contrib.auth import login
from gestionAsociados.models import PeticionAdmision, Pais, DocIdentidad, Negocio, Trabajo, Vivienda, Conyuge, Beneficiario, Familiar, ReferenciaPersonal, Asociacion, DocAnexo, ReciboIngreso, Cuenta, TipoDocIdentidad, Departamento, Municipio


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

        #id
        "var":id
    })
    

def verListaAsociado(request):
    #mostrar datos
    #mostrar= DatosCoop.objects.all()
    mostrar= PeticionAdmision.objects.all()

    #return render(request,'gestionCooperativa/verInfoCoop.html', {'mostrar':mostrar})
    return render(request,'verificarInformacion/verListaAsociado.html', {'mostrar':mostrar})
 