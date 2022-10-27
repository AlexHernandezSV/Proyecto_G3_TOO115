from django.db import models

# Create your models here.
cuota_tipo = [
    (1, 'Apertura'),
    (2, 'Aportacion'),
    (3, 'Educacion')
]

class Cuota(models.Model):
    fecha_inicio = models.DateField(null = True)
    fecha_fin = models.DateField(null = True)
    monto = models.FloatField(null = True)
    tipo = models.IntegerField(
        null = False, blank = False,
        choices = cuota_tipo,
    )

    def __str__(self):
        texto ="{0}, {1}, {2}"
        return texto.format(self.tipo, self.fecha_inicio, self.fecha_fin)