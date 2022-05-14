from ..models import Check
import requests
import datetime
from usuarios.models import Usuario

ip = 'localhost'
puerto = '8000'
def create_check(request, id_usuario):
    
    componente = request['componente']

    usuario = Usuario.objects.get(pk=id_usuario)

    if usuario.esAdmin:

        if componente == 'psicologos':
            r = requests.post('http://'+ip+':'+puerto+'/calificacionesPsicologos/create/1',
            json={
                "nombre":"Psicologo Prueba HealthCheck",
                "promedio_calificaciones": 0.0,
                "cantidad_calificaciones": 0,
                "suma_calificaciones": 0.0
            })

            check = Check(
                funcionando = r.status_code == 200,
                fecha = datetime.datetime.now(), 
                componente = 'psicologos',
                ipAddress = ip
            )
            check.save()
            return check

        elif componente == 'vivienda':
            r = requests.post('http://'+ip+':'+puerto+'/simulacion/crearVivienda/',
            json={
                "nombre":"Vivienda prueba HealthCheck",
                "precio": 1.000,
                "parqueadero": "True",
                "pagoPorSemestre": "True",
                "distanciaAlaUniversidad": 2

            })

            check = Check(
                funcionando = r.status_code == 200,
                fecha = datetime.datetime.now(), 
                componente = 'vivienda',
                ipAddress = ip
            )
            check.save()
            return check


        elif componente == 'usuarios':
            r = requests.post('http://'+ip+':8000/usuarios/',
            json={
            "esAdmin" : "false",
                "nombre" :"usuario Prueba",
                "correo" : "correo@prueba.com",
                "clave" : "clave"

            })

            check = Check(
                funcionando = r.status_code == 200,
                fecha = datetime.datetime.now(), 
                componente = 'usuarios',
                ipAddress = ip
            )
            check.save()
            return check    

    
    

    

def get_checks():
    checks = Check.objects.all()
    return checks

def get_check(id):
    check = Check.objects.get(pk=id)
    return check

