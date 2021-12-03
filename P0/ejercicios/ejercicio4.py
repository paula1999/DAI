# Sucesion de Fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Leer archivo
idLectura = open("in.txt", "r")

for linea in idLectura:
    num = linea

idLectura.close()

# Calcular numero
numFibonacci = fibonacci(int(num))

# Escribir archivo
idEscritura = open("out.txt", "w")
idEscritura.write(str(numFibonacci))
idEscritura.close()