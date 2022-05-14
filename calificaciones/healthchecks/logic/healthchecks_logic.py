from ..models import Check
import requests
import datetime

ip = 'localhost'

def create_check(request):
    componente = request['componente']

    if componente == 'psicologos':
        r = requests.post('http://'+ip+':8000/calificacionesPsicologos/create/1',
         json={
            "nombre":"Psicologo Prueba HealthCheck",
            "promedio_calificaciones": 0.0,
            "cantidad_calificaciones": 0,
            "suma_calificaciones": 0.0
        })

        check = Check(
            funcionando = r.status_code == 200,
            fecha = datetime.datetime.now(), 
            componente = 'psicologos'
        )
        check.save()
        return check

    elif componente == 'vivienda':
        r = requests.post('http://'+ip+':8000/simulacion/crearVivienda/',
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
            componente = 'vivienda'
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
            componente = 'usuarios'
        )
        check.save()
        return check    

    
    

    

def get_checks():
    checks = Check.objects.all()
    return checks

def get_check(id):
    check = Check.objects.get(pk=id)
    return check

