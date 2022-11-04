import datetime
import os
from django.db import models

# Create your models here.

directivo_tipo = [
    ('Presidente', 'Presidente'),
    ('Secretario', 'Secretario')
]

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S:')
    filename = '%s%s' % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    nombreRepresentante =  models.TextField(max_length = 200)
    cargo =  models.TextField(
        null = False, blank = False,
        choices = directivo_tipo,
    )
    firma = models.ImageField(upload_to = filepath, null=True, blank=True)
