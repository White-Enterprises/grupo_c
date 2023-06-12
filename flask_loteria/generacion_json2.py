from loteria import carton,cartones
import json
import os


def generar_json(cantidad):                                    

    path_json = os.path.exists('data/cartones.json')        

    if path_json == False and  cantidad != 0:                 
        cartones_json = [{
        f"Carton {1}": carton()                               
        }]

        archivo = open("data/cartones.json", "w")               
        json.dump(cartones_json, archivo, indent=2)           
        archivo.close()                                      
        if cantidad > 1:                                       
            cartones_list = convertir_a_lista()                  
            cart = cartones(cartones_list, cantidad-1)          
            loteria = convertir_a_json(cart)                    
            return loteria
        else:
            return cartones_json
    
    if path_json:                                             
        cartones_list = convertir_a_lista()                
        cart = cartones(cartones_list, cantidad)            
        loteria = convertir_a_json(cart)                 
        return loteria
    
 
def convertir_a_lista():                                       

    archivo = open("data/cartones.json", "r")                 
    cartones_json = json.load(archivo)         
    archivo.close()
    valor_carton = 0   
    cartones_list = []                                       
    for item in cartones_json:
        valor_carton += 1
        filas = item[f"Carton {valor_carton}"]
                                                                
        cartones_list.append(filas)                             
    return cartones_list    


def convertir_a_json(cart):                                    
    valor_carton = 0                            
    lista = []                                                
    for item in cart:          
        cartones_dic = {}                                       
        valor_carton += 1
        cartones_dic[f"Carton {valor_carton}"] = item  
        lista.append(cartones_dic)
                                                              
    archivo = open("data/cartones.json", "w")                
    json.dump(lista, archivo, indent=2)                         
    archivo.close()                                           



