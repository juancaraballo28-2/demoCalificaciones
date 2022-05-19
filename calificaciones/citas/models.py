from django.db import models
from django.core.signing import Signer

# Create your models here.

class Evento(models.Model):
    signer = Signer('Sinasticto')
    idServicio = models.IntegerField()
    nombreProfesional = models.CharField(max_length=100)
    nombreEstudiante = models.CharField(max_length=100)
    codigoEstudiante = models.CharField(max_length=100)
    edificio = models.CharField(max_length=50)
    salon = models.CharField(max_length=50)
    fecha = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.idServicio)  