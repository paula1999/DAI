import random
import re
import time

######################################################################
# Ejercicio 2 #
######################################################################

# Ordenación por burbuja
def ordenacionBurbuja(lista):
    lista = lista.split(',')
    lista = list(map(int,lista))
    n = len(lista)
    inicio = time.process_time()

    for i in range(n-1):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    tiempo = time.process_time() - inicio

    return lista, tiempo

# Ordenación por selección
def ordenacionSeleccion(lista):
    n = len(lista)
    inicio = time.process_time()

    for i in range(n-1):
        for j in range(i+1,n):
            if lista[i] > lista[j]:
                lista[j], lista[i] = lista[i], lista[j]
    
    tiempo = time.process_time() - inicio

    return lista, tiempo

######################################################################
# Ejercicio 3 #
######################################################################

# Criba de Erastotenes
def cribaErastotenes(n):
    if (n < 0):
        return 'ERROR: entrada incorrecta'

    lista = [True for i in range(n)]
    i = 2

    while(i*i < n):
        if (lista[i]):
            for j in range(i*2, n, i):
                lista[j] = False
        i += 1

    if (n >= 1):
        lista[0] = False
    if (n >= 2):
        lista[1] = False

    primos = []
    j = 0

    for i in range(n):
        if (lista[i]):
            primos.append(j)
        j += 1

    return primos

######################################################################
# Ejercicio 4 #
######################################################################

# Sucesion de Fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


######################################################################
# Ejercicio 5 #
######################################################################

def corchetesAnidados(lista):
    # Contador de parentesis abiertos
    contador = 0

    for i in lista:
        if i == '[':
            contador += 1
        elif i == ']':
            contador -= 1
        
        if contador < 0:
            return "Las parejas de corchetes NO estan correctamente anidados"

    if contador != 0:
        return "Las parejas de corchetes NO estan correctamente anidados"

    return "Las parejas de corchetes SI estan correctamente anidados"


######################################################################
# Ejercicio 6 #
######################################################################

# Identificar cualquier palabra seguida de un espacio y una unica letra mayuscula
def idPalabra (s):
    return re.findall(r"\w+ [A-Z](?!\w)", s)

# Identificar correos electronicos validos
def idCorreoElectronico (s):
    return re.findall(r"[^@ ]+@[^@ ]+\.[^@ ]+", s)

# Identificar numeros de tarjeta de credito 
# cuyos digitos esten separados por - 
# o espacios en blanco cada paquete de cuatro digitos
def idTarjetaCredito (s):
    return re.findall(r"(?<![0-9])([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4})(?![0-9])", s)