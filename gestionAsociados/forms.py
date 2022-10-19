#from socket import fromshare
from django import forms
from gestionAsociados.models import *


class registerAspirantForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30)
    apellido = forms.CharField(label ="Apellido",max_length=30)
    email = forms.EmailField()

class peticionAspiranteForm(forms.Form):
    #Datos personales
    nombre1 = forms.CharField(label="Primer nombre",max_length=30)
    nombre2 = forms.CharField(label="Segundo nombre",max_length=30)
    nombre3 = forms.CharField(label="Tercer nombre",max_length=30)
    apellido1 = forms.CharField(label="Primer apellido",max_length=30)
    apellido2 = forms.CharField(label="Segundo apellido",max_length=30)
    docIdentidad = forms.CharField(label="Documento de Identificación", max_length=20)
    fechaNac = forms.DateField(label="Fecha de nacimiento")
    lugarNac = forms.CharField(label="Lugar de nacimiento",max_length=150)
    direccion = forms.CharField(label="Dirección",max_length=250)
    email = forms.EmailField(label="Email")
    departamento = forms.ModelChoiceField(label="Departamento",queryset=Departamento.objects.all())
    municipio = forms.ModelChoiceField(label="Municipio",queryset=Municipio.objects.all())
    pais = forms.ModelChoiceField(label="País",queryset=Pais.objects.all())
    personasDependientes = forms.IntegerField(label="Nº de Personas que dependen de mí")
    #verificada = forms.BooleanField(label="Verificada",disabled=True)
    #aprobada = forms.BooleanField(label="Aprobada",disabled=True)
    #estado = forms.BooleanField(label="Estado",disabled=True)
    tipoDoc = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocIdentidad.objects.all())
    numero = forms.CharField(label="Documento de Identificación",max_length = 30)
    #Vivienda
    propietario = forms.CharField(label="Propietario",max_length=30,required=False)
    parentesco = forms.CharField(label="Parentesco",max_length=20,required=False)
    tenenciaVivienda = forms.CharField(label="Tenencia de vivienda",max_length=30)
    tiempo = forms.IntegerField(label="Tiempo",)
    ubicacion = forms.CharField(label="Ubicación",max_length=150,required=False)

class DocIdendadForm(forms.Form):
    tipoDoc = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocIdentidad.objects.all())
    numero = models.CharField(max_length = 30)

#Este sirve para las referencias familiares y los padres
class FamiliaresForm(forms.Form):
    parentesco = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()
    municipio= forms.ModelChoiceField(queryset=Municipio.objects.all())
    departamento= forms.ModelChoiceField(queryset=Departamento.objects.all())

class NegocioForm(forms.Form):
    nombreNegocio = forms.CharField(max_length= 30)
    direccion = forms.CharField(max_length=250)
    telefono = forms.CharField(max_length=30)
    email = forms.EmailField()
    numRegistroIva = forms.CharField(max_length = 50)
    giro = forms.CharField(max_length= 150)
    numTrabajadores = forms.IntegerField()
    capital = forms.DecimalField(max_digits=13,decimal_places=4)
    mercancia = forms.DecimalField(max_digits=13,decimal_places=4)
    mobiliarioEquipo = forms.DecimalField(max_digits=12,decimal_places=2)

class TrabajoForm(forms.Form):
    tipo = forms.CharField(max_length=30)
    lugarTrabajo = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=250)
    telefono = forms.CharField(max_length=30)
    email = forms.EmailField()
    sueldo = forms.DecimalField(max_digits=10,decimal_places=4)
    cargo = forms.CharField(max_length=30)
    jefe = forms.CharField(max_length=30)    

class ConyegeForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    docIdentidad = forms.CharField(max_length = 15)
    telefono = forms.CharField(max_length=15)

class ReferenciaPersonalForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()

class BeneficiarioForm(forms.Form):
    parentesco = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    beneficio = forms.DecimalField(max_digits=10,decimal_places=4)

