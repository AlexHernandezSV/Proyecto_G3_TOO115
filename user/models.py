from random import choices
from secrets import choice
from weakref import proxy
from django.db import models
from  django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        ASPIRANTE = "ASPIRANTE", 'Aspirante'
        JEFEOPERACIONES = "JEFEOPERACIONES", 'JefeOperaciones'
        CAJERO = "CAJERO", 'Cajero'
        SOCIO = "SOCIO", 'Socio'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    
    def toJSON(self):
        item = model_to_dict(self)
        return item

class Aspirante(User):
    base_role = User.Role.ASPIRANTE

    class Meta:
        proxy = True

    def welcome(self):
        return "Solo para aspirantes"


class JefeOperaciones(User):
    base_role = User.Role.JEFEOPERACIONES

    class Meta:
        proxy = True

    def welcome(self):
        return "Solo para jefe de operaciones"


class Cajero(User):
    base_role = User.Role.CAJERO

    class Meta:
        proxy = True

    def welcome(self):
        return "Solo para cajero"



class Administrador(User):
    base_role = User.Role.ADMIN

    class Meta:
        proxy = True

    def welcome(self):
        return "Solo para administrador"