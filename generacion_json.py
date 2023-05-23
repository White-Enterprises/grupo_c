from loteria import carton
import json
import os

def agregar(cantidad):
    i = 0
    archivo = open("data/cartones.json", "r")
    cartones_json = json.load(archivo)
    archivo.close()

    while i < cantidad:
        carton_loteria = carton()

        existe = 0
        for item in cartones_json.values():
            print(item)
            if carton_loteria == item:
                existe += 1

        if existe == 0:
            valor_carton = len(cartones_json) +1
            cartones_json[f"Carton {valor_carton}"] = carton_loteria
            i+=1

    archivo = open("data/cartones.json", "w")
    json.dump(cartones_json, archivo)
    archivo.close()

def generar_json(cantidad = 0):

    path_json = os.path.exists('data/cartones.json')

    if path_json:
        # cantidad = int(input("Ingrese la cantidad de cartones a generar: "))
        loteria = agregar(cantidad)
        return loteria
    
    if path_json == False and  cantidad != 0:
        # cantidad = int(input("Ingrese la cantidad de cartones a generar: "))
        cartones_json = {
        f"Carton {1}": carton()
        }

        archivo = open("data/cartones.json", "w")
        json.dump(cartones_json, archivo)
        archivo.close()
        loteria = agregar(cantidad-1)
        return loteria
