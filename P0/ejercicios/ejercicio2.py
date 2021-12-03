import time
import random

# Ordenación por burbuja
def ordenacionBurbuja(lista):
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


n = 10

# Genero matriz aleatoria
A = []

for i in range(n):
    A.append(random.randint(0,50))
    print(A)

ABurbuja, tiempoBurbuja = ordenacionBurbuja(A)
ASeleccion, tiempoSeleccion = ordenacionSeleccion(A)

print("Burbuja: ", ABurbuja, tiempoBurbuja)
print("Seleccion: ", ASeleccion, tiempoSeleccion)