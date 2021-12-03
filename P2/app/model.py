from pickleshare import *

db = PickleShareDB('BD')

# TODO

def usuario_registrado (username):
    return username in db

def get_datos (username):
    # TODO
    if (usuario_registrado(username)):
        return db[username]
    return None

def aniadir_usuario (username, datos):
    # TODO
    if (not usuario_registrado(username)):
        db[username] = datos

def borrar_usuario (username):
    del db[username]