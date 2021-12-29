from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient("mongo", 27017)    # Conectar al servicio (docker) "mongo" en su puerto estandar
db = client.SampleCollections           # Elegimos la base de datos de ejemplo


def get_datos_pokemon():
    pokemon = db.samples_pokemon.find()
    lista = []

    for p in pokemon:
        string_json = dumps(p)     # convertir objeto p a json string
        lista.append(string_json)

    return lista



def get_datos_pokemon_N(N):
    pokemon = db.samples_pokemon.find_one({"id": N})

    if pokemon == None:
        return None

    informacion = ("num", "name", "img", "type", "height", "weight", "weaknesses", "prev_evolution", "next_evolution")

    contenido = {}

    for i in informacion:
        if i in pokemon:
            contenido[i] = pokemon[i]

    return contenido


def aniadir_pokemon(solicitud):
    if db.samples_pokemon.find_one({"id": int(solicitud["num"])}):
        return False
    
    id = int(solicitud["num"])
    num = solicitud["num"]
    name = solicitud["name"]
    img = solicitud["img"]
    type = solicitud["type"]
    height = solicitud["height"]
    weight = solicitud["weight"]
    weaknesses = solicitud["weaknesses"]
    prev_evolution = []
    next_evolution = []

    if "prev_evolution" in solicitud:
        prev_evolution = solicitud["prev_evolution"]
    
    if "next_evolution" in solicitud:
        next_evolution = solicitud["next_evolution"]

    nuevo_pokemon = {"id": id, "num": num, "name": name, "img": img, "type": type, "height": height, "weight": weight, "weaknesses": weaknesses, "prev_evolution": prev_evolution, "next_evolution": next_evolution}
    
    db.samples_pokemon.insert(nuevo_pokemon)

    return True


def modificar_pokemon(solicitud, N):
    if db.samples_pokemon.find_one({"id": int(N)}) == None:
        return False

    # Ya existe otro Pokémon con ese id
    if int(solicitud["num"]) != int(N) and db.samples_pokemon.find({"id": int(solicitud["num"])}).count() != 0:
        return False
    
    solicitud["id"] = int(solicitud["num"])
    db.samples_pokemon.update_one({"id": int(N)}, {"$set": solicitud})

    return True


def borrar_pokemon(N):
    resultado = db.samples_pokemon.delete_one({"num": N})

    if (resultado.deleted_count != 0):
        return True
    else:
        return False