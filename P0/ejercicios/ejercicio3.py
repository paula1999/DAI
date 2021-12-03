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


print(cribaErastotenes(50))