import random
from pprint import pprint as pp

def fila_vacia():                       #Funcion para realizar 1 fila con todos 0(vacia)
    i=0                                 
    fila=[]                             #Creamos la lista de la fila
    while i < 9:
        fila.append(0)                  #agregamos los ceros a la lista
        i+=1
    return fila

def position():                         #Funcion para llenar la lista vacia obtenida en (fila_vacia)
    fila=fila_vacia()                   #llamamos a la funcion fila_vacia
    i=0
    while i < 5:                        #ciclamos 5 veces para obtener la misma cantidad de numeros
        posicion=random.randint(0,8)        #pedimos de forma random un numero de 0 a 8 para obtener la posicion donde se asignara el numero
        if fila[posicion]==0:               #si la posicion es igual a 0 el lugar esta disponible y se puede asignar el numero en esa posicion
            if posicion == 8:               # si la posicion es igual a 8 pide de forma random un numero de 80 a 90 
                num=random.randint(80,90)
                fila[posicion]=num
                i+=1
            else:                           #si la posicion es diferente a 8
                num=random.randint(1,9) + (posicion*10)     #obtenemos de forma random un numero de 1 a 9 que se suma con la posicion y se multiplica por 10
                fila[posicion]=num              # se asigna el numero obtenido de la ecuacion anterior a la posicion obtenida
                i+=1
    return fila

def carton():                           #Funcion para crear el carton
    carton=[]                           #creamos la lista del carton donde se agregaran las filas obtenidas en la funcion position
    i=0
    while i < 3:                        #Ciclamos 3 veces ( 1 por fila del carton )
        fila=position()                 #llamamos a la funcion position 
        carton.append(fila)             #se agrega la fila a la lista carton
        i+=1

    f = 0

# Validador de numeros para que lo numeros obtenidos en la primer fila sean menor a los de la segunda y estos a los de la tercera

    for c in range(len(carton[0])):     # ciclamos una fila en su rango para obtener posiciones de columnas(c) y empezar a validar
        if carton[f][c] and carton[f+1][c] and carton[f+2][c]:          #si la f/c 0 es true y la f 1 c 0 es true y la f2 c 0 es true significa que hay 3 numeros en esa 
                                                                        #columna e ingresa al if para empezar a validar

            #Mientras que el numero de f/c 0 sea mayor al de f1 c0 o el numero f/c 0 sea mayor al de f2 c0 o f1 c0 sea mayor al de f2 c0 va a ciclar
            #generando un numero nuevo a cada posicion true
            while carton[f][c] >= carton[f+1][c] or carton[f][c] >= carton[f+2][c] or carton[f+1][c] >= carton[f+2][c]:            

                num_nuevo=random.randint(1,9) + (c*10)
                carton[f][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+1][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+2][c]=num_nuevo
        
        elif carton[f][c] and carton[f+1][c] and carton[f+2][c] == False:       #si la f/c 0 es true y la f 1 c 0 es true y la f2 c 0 es false significa que hay 2 numeros en esa 
                                                                                #columna e ingresa al if para empezar a validar

            #Mientras que el numero de f/c 0 sea mayor al de f1 c0 va a ciclar generando un numero nuevo a cada posicion true
            while carton[f][c] >= carton[f+1][c]:
            
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+1][c]=num_nuevo
        
        elif carton[f][c] and carton[f+1][c] == False and carton[f+2][c]:       #si la f/c 0 es true y la f 1 c 0 es false y la f2 c 0 es true significa que hay 2 numeros en esa 
                                                                                #columna e ingresa al if para empezar a validar
        
            #Mientras que el numero de f/c 0 sea mayor al de f2 c0 va a ciclar generando un numero nuevo a cada posicion true
            while carton[f][c] >= carton[f+2][c]:
        
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+2][c]=num_nuevo
        
        elif carton[f][c] == False and carton[f+1][c] and carton[f+2][c]:       #si la f/c 0 es false y la f 1 c 0 es true y la f2 c 0 es true significa que hay 2 numeros en esa 
                                                                                #columna e ingresa al if para empezar a validar

            #Mientras que el numero de f1 c0 sea mayor al de f2 c0 va a ciclar generando un numero nuevo a cada posicion true
            while carton[f+1][c] >= carton[f+2][c]:
        
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+1][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+2][c]=num_nuevo
    
    carton_ = carton[0] + carton[1] + carton[2]         #Unifico todas las filas en una sola lista

    return carton_

# cantidad = int(input("Ingrese la cantidad de cartones a generar: "))

def cartones(cartones_list, cantidad):          #Funcion para generar lista de cartones, cartones_list se obtiene de generacion_json con la cantidad a generar
  
    cantidad_list = cartones_list           # lista de cartones ya generada (obtenida del json)
    i = 0
    while i < cantidad:
        carton_generado = carton()          #se genera un nuevo carton
        if not carton_generado in cantidad_list:        #si el carton no existe en la lista lo agrega
            cantidad_list.append(carton_generado)
            i += 1
        print(i)
    return cantidad_list



# i=0
# for item in cartones(cantidad):
#     i+=1
#     print(f"Carton { i } Fila 1: {item[:9]}")
#     print(f"         Fila 2: {item[9:18]}")
#     print(f"         Fila 3: {item[18:27]}")

