from ..models import Usuario

def get_usuario(id):
    usuario = Usuario.objects.using('seguridad').get(pk=id)
    return usuario

def create_usuario(nuevo_usuario):  
    usuario = Usuario(
        esAdmin = nuevo_usuario['esAdmin'],
        nombre = nuevo_usuario['nombre'],
        correo = nuevo_usuario['correo'],
        clave = nuevo_usuario['clave'] 
    )  
    usuario.save(using='seguridad')
    return usuario


    