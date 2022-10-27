from string import digits
from unicodedata import decimal
from django.db import models
from user.models import Aspirante

# Create your models here.

tenencia_viviendaChoices = [
    ('Propia','Propia'),
    ('Alquilada','Alquilada'),
    ('Promesa de venta','Promesa de venta'),
    ('Familiar','Familiar')
]

class Departamento(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Pais(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=30)
    extensionTelefono = models.CharField(blank=True,max_length=10)
    def __str__(self):
        return self.nombre

class TipoDocIdentidad(models.Model):
    nombreDocumento = models.CharField(max_length=30)
    def __str__(self):
        return self.nombreDocumento

class PeticionAdmision(models.Model):
    nombre1 = models.CharField(max_length=30)
    nombre2 = models.CharField(max_length=30)
    nombre3 = models.CharField(blank=True,max_length=30,null=True)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(blank=True,max_length=30)

    fechaNac = models.DateField()
    lugarNac = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    personasDependientes = models.IntegerField()
    verificada = models.BooleanField(blank=True,default=False)
    aprobada = models.BooleanField(blank=True,default=False)
    estado = models.BooleanField(blank=True,default=False)

    aspirante = models.OneToOneField(Aspirante, on_delete=models.CASCADE, blank=True)

    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    
class DocIdentidad(models.Model):
    tipoDoc = models.ForeignKey(TipoDocIdentidad,on_delete=models.CASCADE)
    numero = models.CharField(max_length = 30)
    peticionAdmision = models.OneToOneField(PeticionAdmision,on_delete=models.CASCADE)

    def __str__(self):
        return self.numero

class Negocio(models.Model):
    nombreNegocio = models.CharField(max_length= 30)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    numRegistroIva = models.CharField(max_length = 50)
    giro = models.CharField(max_length= 150)
    numTrabajadores = models.IntegerField()
    capital = models.DecimalField(max_digits=13,decimal_places=4)
    mercancia = models.DecimalField(max_digits=13,decimal_places=4)
    mobiliarioEquipo = models.DecimalField(max_digits=13,decimal_places=4)
    peticionAdmision = models.OneToOneField(PeticionAdmision,on_delete=models.CASCADE)

class Trabajo(models.Model):
    tipo = models.CharField(max_length=30)
    lugarTrabajo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=30)
    email = models.EmailField()
    sueldo = models.DecimalField(max_digits=10,decimal_places=4)
    cargo = models.CharField(max_length=30)
    jefe = models.CharField(max_length=30)
    peticionAdmision = models.OneToOneField(PeticionAdmision,on_delete=models.CASCADE)   

class Vivienda(models.Model):
    propietario = models.CharField(blank=True,max_length=30)
    parentesco = models.CharField(max_length=20)
    tenenciaVivienda = models.CharField(max_length=30,choices=tenencia_viviendaChoices)
    tiempo = models.IntegerField()
    ubicacion = models.CharField(blank=True,max_length=150) #Crear la clase ubicacion
    peticionAdmision = models.OneToOneField(PeticionAdmision,on_delete=models.CASCADE)

class Conyuge(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    docIdentidad = models.CharField(max_length = 15)
    telefono = models.CharField(max_length=15)
    peticionAdmision = models.OneToOneField(PeticionAdmision,on_delete=models.CASCADE)

class Beneficiario(models.Model):
    parentesco = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    beneficio = models.DecimalField(max_digits=12,decimal_places=4)
    peticionAdmision = models.ForeignKey(PeticionAdmision,on_delete=models.CASCADE)

class Familiar(models.Model):
    parentesco = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    municipio= models.ForeignKey(Municipio,on_delete=models.CASCADE)
    departamento= models.ForeignKey(Departamento,on_delete=models.CASCADE)
    peticionAdmision = models.ForeignKey(PeticionAdmision,on_delete=models.CASCADE)


class ReferenciaPersonal(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    peticionAdmision = models.ForeignKey(PeticionAdmision,on_delete=models.CASCADE)

class Asociacion(models.Model):
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length=250)
    peticionAdmision = models.ForeignKey(PeticionAdmision,on_delete=models.CASCADE)

class DocAnexo(models.Model):
    nombre = models.CharField(max_length=50)
    doc = models.FileField(upload_to='documentos',blank=True,null=True)
    peticionAdmision = models.ForeignKey(PeticionAdmision,on_delete=models.CASCADE)

class ReciboIngreso(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=30)
    aspirante = models.OneToOneField(Aspirante,on_delete=models.CASCADE)
class Cuenta(models.Model):
    codigo=models.CharField(max_length=8)
    tipo=models.CharField(max_length=10)
    saldo=models.DecimalField(max_digits=10, decimal_places = 2)
    aspirante = models.ForeignKey(Aspirante,on_delete=models.CASCADE)

class Expediente():
    pass
class Foto():
    foto = models.ImageField()
    aspirante= models.OneToOneField(Aspirante,on_delete=models.CASCADE)
