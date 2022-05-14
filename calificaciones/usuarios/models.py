from django.db import models

class Usuario(models.Model):
    esAdmin = models.BooleanField()
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=100)
