from loteria import carton,cartones
import json
import os


def generar_json(cantidad):                                     #funcion para generar el json, cantidad es el valor que viene del input

    path_json = os.path.exists('data/cartones.json')            #variable boolean para saber si existe el archivo json

    if path_json == False and  cantidad != 0:                   # si path_json es falso (no existe) y la cantidad es distinta a 0 se crea el diccionario con el formato del json con solo 1 carton
        cartones_json = {
        f"Carton {1}": carton()                                 #carton() llama a la misma funcion del archivo loteria.py
        }

        archivo = open("data/cartones.json", "w")               #abrimos el cartones.json en formato solo escritura (w)
        json.dump(cartones_json, archivo, indent=2)             #escribimos el contenido de la variable cartones_json
        archivo.close()                                         #cerramos el json
        if cantidad > 1:                                        #Si el json no existe y la cantidad es mayor a 1 utilizamos la funcion convertir a lista para agregar el resto de los cartones
            cartones_list = convertir_a_lista()                  
            cart = cartones(cartones_list, cantidad-1)          # la cantidad es -1 porque ya agregamos el primer carton con cartones_json
            loteria = convertir_a_json(cart)                    #una vez agregados los cartones a la lista volvemos a generar el json
            return loteria
        else:
            return cartones_json
    
    if path_json:                                               #si el path_json es true (cartones.json existe) 
        cartones_list = convertir_a_lista()                     #llamamos a la funcion convertir a lista que nos retornara una lista de los cartones del json
        cart = cartones(cartones_list, cantidad)                #llamamos la funcion cartones que agregara los nuevos cartones y le pasamos por parametro la lista obtenida con la cantidad
        loteria = convertir_a_json(cart)                        #llamamos a la funcion convertir a json y le pasamos por parametro la lista obtenida con los cartones nuevos ya agregados
        return loteria
    
 
def convertir_a_lista():                                        #Funcion para convertir el json a una lista

    archivo = open("data/cartones.json", "r")                   #abrimos el json en formato solo lectura (r)
    cartones_json = json.load(archivo)                          #lo carga en la variable cartones_json
    archivo.close()

    cartones_list = []                                          #creamos una lista donde pondremos las listas de cartones que estan en el json
    for filas in cartones_json.values():                        #obtenemos solo los valores
        cartones_list.append(filas)                             
    return cartones_list    


def convertir_a_json(cart):                                     #funcion para convertir la lista a json
    valor_carton = 0                            
    cartones_dic = {}                                           #creamos el diccionario que posteriormente sera nuestro json
    for item in cart:                                           #ciclamos la lista de listas con los cartones obtenidos
        valor_carton += 1
        cartones_dic[f"Carton {valor_carton}"] = item           #agregamos al diccionario cartones_dic el numero del carton con los valores correspondientes
    archivo = open("data/cartones.json", "w")                   #abrimos el cartones.json en formato solo escritura (w)
    json.dump(cartones_dic, archivo, indent=2)                  #escribimos el contenido de la variable cartones_json
    archivo.close()                                             ##cerramos el json



