from django.db import models

class Check(models.Model):
    funcionando = models.BooleanField()
    fecha = models.DateTimeField()
    componente = models.CharField(max_length=100)