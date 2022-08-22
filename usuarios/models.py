from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255, null=True, blank=True ,name="telefono")
    edad = models.PositiveIntegerField(null=True, blank=True ,name="edad")
    provincia = models.CharField(max_length=255, null=True, blank=True, name="provincia")
    localidad = models.CharField(max_length=255, null=True, blank=True, name="localidad")
    direccion = models.CharField(max_length=255, null=True, blank=True, name="direccion")
    

    def __str__(self):
        return self.first_name