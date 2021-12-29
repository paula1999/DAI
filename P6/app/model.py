from pickleshare import *

db_pickleshare = PickleShareDB('BD')


def usuario_registrado (username):
    return username in db_pickleshare

def get_datos (username):
    if (usuario_registrado(username)):
        return db_pickleshare[username]
    return None

def aniadir_usuario (username, datos):
    if (not usuario_registrado(username)):
        db_pickleshare[username] = datos

def borrar_usuario (username):
    del db_pickleshare[username]