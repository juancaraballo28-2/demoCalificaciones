
from ..models import Psicologo, Calificacion
from usuarios.models import Usuario

def get_psicologo(id):
    psicologo = Psicologo.objects.get(pk=id)
    return psicologo

def create_psicologo(nuevo_psicologo, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)
    if usuario.esAdmin:
        psicologo = Psicologo(nombre=nuevo_psicologo["nombre"], 
        promedio_calificaciones=nuevo_psicologo["promedio_calificaciones"], 
        cantidad_calificaciones=nuevo_psicologo["cantidad_calificaciones"], 
        suma_calificaciones=nuevo_psicologo["suma_calificaciones"])
        psicologo.save()
        return psicologo  
    else:
        psicologo = Psicologo(nombre='Usuario no autorizado', 
        promedio_calificaciones=None, 
        cantidad_calificaciones=None, 
        suma_calificaciones=None)
        return psicologo 

    

def delete_psicologo(id, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)
    if usuario.esAdmin:
        psicologo = Psicologo.objects.get(pk=id)
        psicologo.delete()
        return psicologo
    else:
        psicologo = Psicologo(nombre='Usuario no autorizado', 
        promedio_calificaciones=None, 
        cantidad_calificaciones=None, 
        suma_calificaciones=None)
        return psicologo     
    

def add_calificacionpsicologo(id, puntuacion):
    psicologo = Psicologo.objects.get(pk=id)
    psicologo.suma_calificaciones += puntuacion
    psicologo.cantidad_calificaciones += 1 
    psicologo.promedio_calificaciones =  psicologo.suma_calificaciones / psicologo.cantidad_calificaciones
    psicologo.save() 
    return psicologo


def get_calificaciones():
    calificaciones = Calificacion.objects.all()
    return calificaciones

def get_calificacion(id):
    calificaciones = Calificacion.objects.get(id)
    return calificaciones    

def create_calificacion(nueva_calificacion, id_psicologo):
    calificacion = Calificacion(psicologo=get_psicologo(id_psicologo), mensaje=nueva_calificacion["mensaje"], puntuacion = nueva_calificacion["puntuacion"])
    calificacion.save()
    add_calificacionpsicologo(id_psicologo,nueva_calificacion["puntuacion"])
    return calificacion