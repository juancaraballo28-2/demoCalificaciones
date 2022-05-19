
from ..models import Evento
from django.core.signing import Signer

def get_cita(id):
    cita = Evento.objects.get(pk=id)
    return cita

def create_cita(nuevaCita):
    signer = Signer('Sinasticto')
    cita = Evento(idServicio=nuevaCita["idServicio"], 
    nombreProfesional=signer.sign(nuevaCita["nombreProfesional"]), 
    nombreEstudiante=signer.sign(nuevaCita["nombreEstudiante"]), 
    codigoEstudiante=signer.sign(nuevaCita["codigoEstudiante"]),
    edificio=signer.sign(nuevaCita["edificio"]),
    salon=signer.sign(nuevaCita["salon"]),
    fecha=signer.sign(nuevaCita["fecha"]),)
    cita.save()
    return cita 