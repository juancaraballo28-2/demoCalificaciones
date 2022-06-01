from django.db import models

class Token(models.Model):
    token = models.TextField()
    fecha = models.DateTimeField()
