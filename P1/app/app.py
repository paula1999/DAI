#./app/app.py
from flask import Flask, render_template
from ejercicio1 import *
from random import randint

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

######################################################################
# Ejercicio 1 #
######################################################################

# Ordenacion burbuja
@app.route('/ordenacionBurbuja/<lista>')
def ordenarBurbuja(lista):
    lista, tiempo = ordenacionBurbuja(lista)
    lista = list(map(str,lista))
    lista = ', '.join(lista)
    
    return "Lista ordenada con burbuja: " + lista + " Tiempo: " + str(tiempo)

# Ordenacion seleccion
@app.route('/ordenacionSeleccion/<lista>')
def ordenarSeleccion(lista):
    lista, tiempo = ordenacionSeleccion(lista)
    lista = list(map(str,lista))
    lista = ', '.join(lista)

    return "Lista ordenada con selección: " + lista + " Tiempo: " + str(tiempo)

# Erastotenes
@app.route('/cribaErastotenes/<n>')
def erastotenes(n):
    lista = cribaErastotenes(int(n))
    lista = list(map(str,lista))
    lista = ', '.join(lista)
    return "Criba de Erastotenes: " + lista

# Fibonacci
@app.route('/fibonacci/<n>')
def fib(n):
    return "Fibonacci: " + str(fibonacci(int(n)))

# Corchetes anidados
@app.route('/corchetesAnidados/<lista>')
def corchetes(lista):
    return corchetesAnidados(lista)
    
# Identificar palabra
@app.route('/idPalabra/<s>')
def identificarPalabra(s):
    return ', '.join(idPalabra(s))

# Identificar correo electronico
@app.route('/idCorreoElectronico/<s>')
def identificarCorreo(s):
    return ', '.join(idCorreoElectronico(s))

# Identificar tarjeta de credito
@app.route('/idTarjetaCredito/<s>')
def identificarTarjeta(s):
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