import re

# Identificar cualquier palabra seguida de un espacio y una unica letra mayuscula
def idPalabra (s):
    return re.findall(r"\w+ [A-Z](?!\w)", s)

# Identificar correos electronicos validos
def idCorreoElectronico (s):
    return re.findall(r"[^@ ]+@[^@ ]+\.[^@ ]+", s)

# Identificar numeros de tarjeta de credito 
# cuyos digitos esten separados por - 
# o espacios en blanco cada paquete de cuatro digitos
def idTarjetaCreditos (s):
    return re.findall(r"(?<![0-9])([0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4})(?![0-9])", s)

# Pruebas
print(idPalabra("asjiodajd aijdaid a qijwne iaidna A cnuciq ja J"))
print(idCorreoElectronico("pijsdiaj@gmail.com"))
print(idTarjetaCreditos("1234 5678 9012 3456"))