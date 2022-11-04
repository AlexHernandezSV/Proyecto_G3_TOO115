#from socket import fromshare
from turtle import textinput
from xml.parsers.expat import model
from django import forms
from django.forms import modelformset_factory
from gestionAsociados.models import *

tenencia_viviendaChoices = [
    ('Propia','Propia'),
    ('Alquilada','Alquilada'),
    ('Promesa de venta','Promesa de venta'),
    ('Familiar','Familiar')
]

class registerAspirantForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=30)
    apellido = forms.CharField(label ="Apellido",max_length=30)
    email = forms.EmailField()

class peticionAspiranteForm(forms.Form):
    #Datos personales
    nombre1 = forms.CharField(label="Primer nombre",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    nombre2 = forms.CharField(label="Segundo nombre",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    nombre3 = forms.CharField(label="Tercer nombre",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido1 = forms.CharField(label="Primer apellido",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido2 = forms.CharField(label="Segundo apellido",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    tipoDoc = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocIdentidad.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))
    numeroDoc = forms.CharField(label="Numero de documento",max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    fechaNac = forms.DateField(label="Fecha de nacimiento",widget=forms.DateInput(attrs={"class":"form-control"}))
    lugarNac = forms.CharField(label="Lugar de nacimiento",max_length=150,widget=forms.TextInput(attrs={"class":"form-control"}))
    direccion = forms.CharField(label="Dirección",max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    departamento = forms.ModelChoiceField(label="Departamento",queryset=Departamento.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))
    municipio = forms.ModelChoiceField(label="Municipio",queryset=Municipio.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))
    pais = forms.ModelChoiceField(label="País",queryset=Pais.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))
    personasDependientes = forms.IntegerField(label="Nº de Personas que dependen de mí",widget=forms.TextInput(attrs={"class":"form-control"}))
    #verificada = forms.BooleanField(label="Verificada",disabled=True)
    #aprobada = forms.BooleanField(label="Aprobada",disabled=True)
    #estado = forms.BooleanField(label="Estado",disabled=True)

class DocIdentidadForm(forms.Form):
    tipoDoc = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocIdentidad.objects.all())
    numero = forms.CharField(label='Numero de documento',max_length = 30)

#Este sirve para las referencias familiares y los padres
class FamiliaresForm(forms.Form):
    parentescoFamiliar = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    nombreFamiliar = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    apellidoFamiliar = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    telefonoFamiliar = forms.CharField(max_length=15,widget=forms.TextInput(attrs={"class":"form-control"}))
    emailFamiliar = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    municipioFamiliar= forms.ModelChoiceField(queryset=Municipio.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))
    departamentoFamiliar= forms.ModelChoiceField(queryset=Departamento.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))

class NegocioForm(forms.Form):
    nombreNegocio = forms.CharField(max_length= 30,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    direccionNegocio = forms.CharField(max_length=250,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    telefonoNegocio = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    emailNegocio = forms.EmailField(required=False,widget=forms.EmailInput(attrs={"class":"form-control"}))
    numRegistroIva = forms.CharField(max_length = 50,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    giro = forms.CharField(max_length= 150,required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    numTrabajadores = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={"class":"form-control"}))
    capital = forms.DecimalField(max_digits=13,decimal_places=4,required=False,widget=forms.NumberInput(attrs={"class":"form-control"}))
    mercancia = forms.DecimalField(max_digits=13,decimal_places=4,required=False,widget=forms.NumberInput(attrs={"class":"form-control"}))
    mobiliarioEquipo = forms.DecimalField(max_digits=12,decimal_places=2,required=False,widget=forms.NumberInput(attrs={"class":"form-control"}))

class TrabajoForm(forms.Form):
    tipo = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    lugarTrabajo = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    direccionTrabajo= forms.CharField(required=False,max_length=250,widget=forms.TextInput(attrs={"class":"form-control"}))
    telefonoTrabajo = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    emailTrabajo = forms.EmailField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    sueldo = forms.DecimalField(required=False,max_digits=10,decimal_places=4,widget=forms.TextInput(attrs={"class":"form-control"}))
    cargo = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    jefe = forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))    

class ConyegeForm(forms.Form):
    nombreC = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    apellidoC = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    docIdentidadC = forms.CharField(max_length = 15,widget=forms.TextInput(attrs={"class":"form-control"}))
    telefonoC = forms.CharField(max_length=15,widget=forms.TextInput(attrs={"class":"form-control"}))

class ReferenciaPersonalForm(forms.Form):
    nombreRef = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    apellidoRef = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    telefonoRef = forms.CharField(max_length=15,widget=forms.TextInput(attrs={"class":"form-control"}))
    emailRef = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))

class BeneficiarioForm(forms.Form):
    parentescoBeneficiario = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    nombreBeneficiario = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    apellidoBeneficiario = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    beneficio = forms.DecimalField(max_digits=10,decimal_places=4,widget=forms.NumberInput(attrs={"class":"form-control"}))

class ViviendaForm(forms.Form):
    propietario = forms.CharField(label='Propietario',max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    parentesco = forms.CharField(label='Parentesco',max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    tenenciaVivienda = forms.ChoiceField(label='Tenencia de vivieda',choices=tenencia_viviendaChoices,widget=forms.Select(attrs={"class":"form-select"}))
    tiempo = forms.CharField(label='Tiempo',max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    #ubicacion = forms.CharField(label='Ubicacion',max_length=30,widget=forms.TextInput(attrs={"class":"form-control"}))
    lat = forms.CharField(label='Seleccione Ubicacion',max_length=30, widget=forms.TextInput(attrs={"class":"form-control",'hidden':'true'}))
    lng = forms.CharField(label='',max_length=30,widget=forms.TextInput(attrs={"class":"form-control",'hidden':'true'}))

class DocAnexoForm(forms.Form):
    nombreDocAnexo = forms.CharField(label='Nombre del documento',max_length=30,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    docAnexo = forms.FileField(label='Doc',max_length=30,required=False)

BeneficiarioFormSet = modelformset_factory(
    Beneficiario,
    exclude=('peticionAdmision',),
    extra=2,
    max_num=5,
    widgets={
        'parentesco': forms.TextInput(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'apellido': forms.TextInput(attrs={'class':'form-control'}),
        'beneficio': forms.NumberInput(attrs={'class':'form-control'}),
    }
)

class ChangePasswordForm(forms.Form):
    passActual= forms.CharField(label='Contraseña Actual',widget=forms.TextInput(attrs={'class':'form-control'}))
    nueva= forms.CharField(label='Contraseña nueva',widget=forms.TextInput(attrs={'class':'form-control'}))
    repetir= forms.CharField(label='Repetir contraseña nueva',widget=forms.TextInput(attrs={'class':'form-control'}))
