#./app/app.py
# Paula Villanueva Nuñez

from flask import Flask, render_template, flash, redirect, request, url_for, session, jsonify
from ejercicio1 import *
from random import randint
from model import *
from model_pokemon import *


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['JSON_AS_ASCII'] = False     # Se muestran tildes



def hello_world():
    return 'Hello, World!'

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('interface.html')




######################################################################
# Formulario #
######################################################################

@app.route('/mongo', methods=['GET', 'POST'])
def mongo():
    if (request.method == 'POST'):
        # Encontramos los documentos de la coleccion "samples_pokemon"
        if 'numero' in request.form:
            pokemon = db.samples_pokemon.find({"num": request.form['numero']}) # devuelve un cursor(*), no una lista ni un iterador
        elif 'nombre' in request.form:
            pokemon = db.samples_pokemon.find({"name": request.form['nombre']}) # devuelve un cursor(*), no una lista ni un iterador
        elif 'tipo' in request.form:
            pokemon = db.samples_pokemon.find({"type": request.form['tipo']}) # devuelve un cursor(*), no una lista ni un iterador
        else: # Mostrar todos
            pokemon = db.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador

    else:
        pokemon = db.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador

    pokemon.sort("id")
    lista_pokemon = []
        
    for p in pokemon:
        app.logger.debug(p) # salida consola
        lista_pokemon.append(p)

    # a los templates de Jinja hay que pasarle una lista, no el cursor
    return render_template('mongo.html', pokemon=lista_pokemon)





######################################################################
# API RESTFull #
######################################################################

'''
API RESTFull:

GET     /pokemon        Devuelve todos los pokemon
GET     /pokemon/N      Devuelve un solo pokemon con el id = N
POST    /pokemon        Crea un pokemon
PUT     /pokemon/N      Actualiza la información del pokemon con el id = N   
DELETE  /pokemon/N      Elimina el pokemon con el id = N
'''


@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    lista = get_datos_pokemon()
    
    return jsonify(lista), 200


@app.route('/pokemon/<N>', methods=['GET'])
def get_pokemon_N(N):
    pokemon = get_datos_pokemon_N(int(N))

    if pokemon == None:
        return jsonify({"ERROR": "No se ha podido encontrar el Pokémon"}), 404
    else:
        return jsonify(pokemon), 200


@app.route('/pokemon', methods=['POST'])
def post_pokemon():
    solicitud = request.get_json()

    if solicitud == None:
        return jsonify({"ERROR": "No se ha podido crear el Pokémon, no hay datos de entrada"}), 404

    if aniadir_pokemon(solicitud):
        return jsonify({"OK": "Pokémon creado correctamente"}), 201
    else:
        return jsonify({"ERROR": "No se ha podido crear el Pokémon, ya existe un Pokémon con ese id"}), 404


@app.route('/pokemon/<N>', methods=['PUT'])
def put_pokemon(N):
    solicitud = request.get_json()

    if solicitud == None:
        return jsonify({"ERROR": "No se ha podido crear el Pokémon, no hay datos de entrada"}), 404


    if modificar_pokemon(solicitud, N):
        return jsonify({"OK": "Pokémon actualizado correctamente"}), 200
    else:
        return jsonify({"ERROR": "No se ha podido modificar el Pokémon"}), 404

@app.route('/pokemon/<N>', methods=['DELETE'])
def delete_pokemon(N):
    if borrar_pokemon(N):
        return jsonify({"OK": "Pokémon borrado correctamente"}), 200
    else:
        return jsonify({"ERROR": "No se ha podido borrar el Pokémon"}), 404



######################################################################
# Flashing #
######################################################################

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    error = None
    
    if (usuario_registrado(username)):
        if (password == get_datos(username)['password']):
            session['username'] = username
            session['historial'] = []
            session['url'] = []
        else:
            error = 'Contraseña incorrecta'
    else:
        error = 'Ese usuario no está registrado'

    args = {'username': username, 'error': error}

    return render_template('login.html', **args)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']

        if (not usuario_registrado(username)):
            session['username'] = username
            session['historial'] = []
            session['url'] = []
            datos = {'password': password, 'nombre': nombre, 'apellidos': apellidos}

            aniadir_usuario(username, datos)

            flash('Usuario registrado correctamente')
        else:
            flash('El usuario ya está registrado')
        
        return redirect(url_for('home'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session['username'] = ''
    session['historial'] = ''
    session['url'] = ''

    flash('Sesión cerrada correctamente')
    
    return redirect(url_for('home'))

@app.route('/user')
def user():
    aniadir_historial('Usuario', request.url)

    return render_template('user.html', username = get_datos(session['username']))

@app.route('/editar_usuario', methods=['GET', 'POST'])
def editar_usuario():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']

        if (not usuario_registrado(username) or username == session['username']):
            borrar_usuario(session['username'])
            session['username'] = username
            datos = {'password': password, 'nombre': nombre, 'apellidos': apellidos}

            aniadir_usuario(username, datos)

            flash('Usuario modificado correctamente')

            return redirect(url_for('home'))
        else:
            flash('El nombre de usuario ya existe, introduce otro por favor')

            return redirect(url_for('editar_usuario'))

    return render_template('editar_usuario.html', username = get_datos(session['username']))

@app.route('/eliminar_usuario')
def eliminar_usuario():
    borrar_usuario(session['username'])

    session['username'] = ''
    session['historial'] = ''
    session['url'] = ''

    flash('Usuario eliminado correctamente')

    return redirect(url_for('home'))

def aniadir_historial(nombre_pagina, url):
    if ('historial' in session and session['username'] != ''):
        session['historial'] = [nombre_pagina] + session['historial']
        session['url'] = [url] + session['url']

        if (len(session['historial']) > 3):
            session['historial'].pop(3)
            session['url'].pop(3)

@app.route('/SWAD')
def swad():
    aniadir_historial('SWAD', request.url)

    return redirect('https://swad.ugr.es/es')

@app.route('/Prado')
def prado():
    aniadir_historial('Prado 21-22', request.url)

    return redirect('https://pradogrado2122.ugr.es/')

######################################################################
# Ejercicio 1 #
######################################################################

# Ordenacion burbuja
@app.route('/ordenacionBurbuja/<lista>')
def ordenarBurbuja(lista):
    aniadir_historial('Ordenación burbuja', request.url)

    lista, tiempo = ordenacionBurbuja(lista)
    lista = list(map(str,lista))
    lista = ', '.join(lista)
    
    return "Lista ordenada con burbuja: " + lista + " Tiempo: " + str(tiempo)

# Ordenacion seleccion
@app.route('/ordenacionSeleccion/<lista>')
def ordenarSeleccion(lista):
    aniadir_historial('Ordenacion seleccion', request.url)

    lista, tiempo = ordenacionSeleccion(lista)
    lista = list(map(str,lista))
    lista = ', '.join(lista)

    return "Lista ordenada con selección: " + lista + " Tiempo: " + str(tiempo)

# Erastotenes
@app.route('/cribaErastotenes/<n>')
def erastotenes(n):
    aniadir_historial('Criba de Erastótenes', request.url)

    lista = cribaErastotenes(int(n))
    lista = list(map(str,lista))
    lista = ', '.join(lista)
    return "Criba de Erastotenes: " + lista

# Fibonacci
@app.route('/fibonacci/<n>')
def fib(n):
    aniadir_historial('Fibonacci', request.url)

    return "Fibonacci: " + str(fibonacci(int(n)))

# Corchetes anidados
@app.route('/corchetesAnidados/<lista>')
def corchetes(lista):
    aniadir_historial('Corchetes anidados', request.url)

    return corchetesAnidados(lista)
    
# Identificar palabra
@app.route('/idPalabra/<s>')
def identificarPalabra(s):
    aniadir_historial('Identificar palabra', request.url)

    return ', '.join(idPalabra(s))

# Identificar correo electronico
@app.route('/idCorreoElectronico/<s>')
def identificarCorreo(s):
    aniadir_historial('Identificar correo electrónico', request.url)

    return ', '.join(idCorreoElectronico(s))

# Identificar tarjeta de credito
@app.route('/idTarjetaCredito/<s>')
def identificarTarjeta(s):
    aniadir_historial('Identificar tarjeta de crédito', request.url)

    return ', '.join(idTarjetaCredito(s))



######################################################################
# Ejercicio 2 #
######################################################################

# Acceder a http://localhost:5000/static/home.html




######################################################################
# Ejercicio 3 #
######################################################################

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404




######################################################################
# Ejercicio EXTRA #
######################################################################

@app.route('/imagenSVG')
def imgSVG():
    aniadir_historial('imagenSVG', request.url)

    color = ["blue", "yellow", "lime", "purple", "black"]
    i = randint(1,3)
    width = randint(500, 900)
    height = randint(500, 900)
    fill = color[randint(0,4)]
    stroke = color[randint(0,3)]
    strokewidth = color[randint(0,4)]
    cx = randint(100,350)
    cy = randint(100,350)
    figura = "<svg width=\"" + str(width) + "\" height=\"" + str(height) + "\">\n"
    

    if (i == 1): # circulo
        r = randint(20,50)

        figura = figura + "<circle cx=\"" + str(cx) + "\" cy=\"" + str(cy) + "\" r=\"" + str(r) + "\" stroke=\"" + stroke + "\" stroke-width=\"" + strokewidth + "\" fill=\"" + fill + "\" /> </svg>"
    if (i == 2): # rectangulo
        width = randint(20,60)
        height = randint(50,100)

        figura = figura + "<rect x=\"" + str(cx) + "\" y=\"" + str(cy) + "\" width=\"" + str(width) + "\" height=\"" + str(height) + "\" style=\"fill:" + fill + ";stroke-width:" + strokewidth + ";stroke:" + stroke + "\" /> </svg>"
    if (i == 3): # elipse
        width = randint(20,60)
        height = randint(50,100)
        rx = randint(20,100)
        ry = randint(20,100)

        figura = figura + "<ellipse cx=\"" + str(cx) + "\" cy=\"" + str(cy) + "\" rx=\"" + str(rx) + "\" ry=\"" + str(ry) + "\" style=\"fill:" + fill + ";stroke:" + stroke + ";stroke:" + strokewidth + "\" /> </svg>"

    
    return "<!DOCTYPE html>\n<html>\n<head></head>\n<body>" + figura + "</body>\n</html>"
