from django.db import models
import datetime
import os

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('pictures/', filename)

class DatosCoop(models.Model):
    nombre_text = models.CharField(max_length=200)
    departamento_text = models.CharField(max_length=200)
    municipio_text = models.CharField(max_length=200)
    numeroRegistro_text = models.CharField(max_length=200)
    aniosFuncionando_numero = models.IntegerField()
    numeroEmpleados_numero = models.IntegerField()
    descripcion_text = models.CharField(max_length=200)
    logo_img = models.ImageField(upload_to=filepath, null=True, blank=True)
    def save(self):
        # contar los objetos de la db
        count = DatosCoop.objects.all().count()
        # ver si variable existe 
        save_permission = DatosCoop.has_add_permission(self)

        # si hay mas de una fila no guardar
        if count < 1:
            super(DatosCoop, self).save()
        elif save_permission:
            super(DatosCoop, self).save()

    def has_add_permission(self):
        return DatosCoop.objects.filter(id=self.id).exists()