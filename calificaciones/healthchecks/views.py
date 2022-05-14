from django.shortcuts import render
from .logic import healthchecks_logic as hl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_healthcheck_view(request, id):
    if request.method == 'GET':
        healthcheck_dto = hl.get_check(id)
        healthcheck = serializers.serialize('json',[healthcheck_dto,])
        return HttpResponse(healthcheck, 'application/json')

@csrf_exempt
def post_healthcheck_view(request, id_usuario):
    if request.method == 'POST':
        healthcheck_dto = hl.create_check(json.loads(request.body), id_usuario)
        print(healthcheck_dto)
        healthcheck = serializers.serialize('json', [healthcheck_dto,])
        return HttpResponse(healthcheck, 'application/json')