from .logic import calificacionespsicologos_logic as cl
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@csrf_exempt
@api_view(['GET'])
def psicologo_view(request,id):
    if request.method == 'GET':
        psicologo_dto = cl.get_psicologo(id)
        psicologo = serializers.serialize('json',[psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

    
@csrf_exempt
@api_view(['POST'])
def psicologo_view_noid(request, id_usuario):
    if request.method == 'POST':
        psicologo_dto = cl.create_psicologo(json.loads(request.body), id_usuario)
        psicologo = serializers.serialize('json', [psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')

@csrf_exempt
def delete_psicologo_view(request, id,  id_usuario):
    if request.method == 'DELETE':
        psicologo_dto = cl.delete_psicologo(id, id_usuario)
        psicologo = serializers.serialize('json', [psicologo_dto,])
        return HttpResponse(psicologo, 'application/json')        

@csrf_exempt
def calificacion_view(request,id_psicologo):
    if request.method == 'POST':
        calificacion_dto = cl.create_calificacion(json.loads(request.body),id_psicologo)
        calificacion = serializers.serialize('json', [calificacion_dto,])
        return HttpResponse(calificacion, 'application/json')
