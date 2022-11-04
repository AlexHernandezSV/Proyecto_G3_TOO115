from django.contrib import admin
from gestionAsociados.models import *
from django.contrib.auth.models import User

# Register your models here.
#admin.site.register(PeticionAdmision)
admin.site.register(Pais)
admin.site.register(Departamento)
admin.site.register(Beneficiario)
admin.site.register(Familiar)
admin.site.register(Trabajo)
admin.site.register(Negocio)
admin.site.register(DocIdentidad)
admin.site.register(Conyuge)
admin.site.register(Vivienda)
admin.site.register(ReferenciaPersonal)
admin.site.register(DocAnexo)
admin.site.register(Asociacion)
admin.site.register(TipoDocIdentidad)
admin.site.register(Municipio)
admin.site.register(ReciboIngreso)
admin.site.register(User)
admin.site.register(Cuenta)

class DocIdentidadAdmin(admin.StackedInline):
    model=DocIdentidad

class ReferenciaPersonalAdmin(admin.TabularInline):
    model = ReferenciaPersonal
class FamiliarAdmin(admin.TabularInline):
    model = Familiar
class ConyugeAdmin(admin.StackedInline):
    model = Conyuge
class ViviendaAdmin(admin.StackedInline):
    model = Vivienda

class DocAnexoAdmin(admin.TabularInline):
    model = DocAnexo

class BeneficiarioAdmin(admin.TabularInline):
    model = Beneficiario
class TrabajoAdmin(admin.StackedInline):
    model = Trabajo

class NegocioAdmin(admin.StackedInline):
    model = Negocio

class PeticionAdmisionAdmin(admin.ModelAdmin):
    inlines = [
        DocIdentidadAdmin,
        ViviendaAdmin,
        ConyugeAdmin,
        ReferenciaPersonalAdmin,
        FamiliarAdmin,
        TrabajoAdmin,
        NegocioAdmin,
        BeneficiarioAdmin,
        DocAnexoAdmin
    ]

admin.site.register(PeticionAdmision,PeticionAdmisionAdmin)