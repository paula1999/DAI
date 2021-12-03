import random

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

# Generar aleatoriamente una cadena de [ y ]
n = 10
lista = []

for i in range(n):
    lista.append(random.choice(["[", "]"]))

print("Lista: ", lista)
print(corchetesAnidados(lista))