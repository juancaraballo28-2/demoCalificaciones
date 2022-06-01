import requests
import json
import datetime
from ..models import Token
def crear_token_acceso():
    

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }

    data = 'grant_type=client_credentials&client_id=O7U6bLAJCkz9tOXqmdTA9tmDcd9tW9GC&client_secret=C5HALHO8TnUlOqrOahMSnKC395hw_KRcQkT-wfmGAMxbk0ZjwjDL-kJAnE4RsuTJ&audience=https://consultarpsicologos/api'

    response = requests.post('https://dev-hbxmjpgk.us.auth0.com/oauth/token', headers=headers, data=data)

    data = json.loads(response.content)

    save_token(data)
    
    return data


def get_token(id):
    token = Token.objects.using('seguridad').get(pk=id)
    return token

def save_token(nuevo_token):
    token = Token(
        token = nuevo_token["access_token"],
        fecha = datetime.datetime.now()
    )
    token.save(using='seguridad')
    return token