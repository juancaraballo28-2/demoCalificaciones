from django.shortcuts import render
from .logic import usuarios_logic as ul
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def usuario_view(request,id):
    if request.method == 'GET':
        usuario_dto = ul.get_usuario(id)
        usuario = serializers.serialize('json',[usuario_dto,])
        return HttpResponse(usuario, 'application/json')


@csrf_exempt
def post_usuario_view(request):
    if request.method == 'POST':
        usuario_dto = ul.create_usuario(json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')
