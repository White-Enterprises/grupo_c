import random
from pprint import pprint as pp

def fila_vacia():
    i=0
    fila=[]
    while i < 9:
        fila.append(0)
        i+=1
    return fila

def position():
    fila=fila_vacia()
    i=0
    while i < 5:
        posicion=random.randint(0,8)
        if fila[posicion]==0:
            if posicion == 8:
                num=random.randint(80,90)
                fila[posicion]=num
                i+=1
            else:
                num=random.randint(0,9) + (posicion*10)
                fila[posicion]=num
                i+=1
    return fila

def carton():
    carton=[]
    i=0
    while i < 3:
        fila=position()
        carton.append(fila)
        i+=1

    f = 0
    for c in range(len(carton[0])):
        if carton[f][c] and carton[f+1][c] and carton[f+2][c]: 
        
            while carton[f][c] >= carton[f+1][c] or carton[f][c] >= carton[f+2][c] or carton[f+1][c] >= carton[f+2][c]:

                num_nuevo=random.randint(1,9) + (c*10)
                carton[f][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+1][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+2][c]=num_nuevo
        
        elif carton[f][c] and carton[f+1][c] and carton[f+2][c] == False:
          
            while carton[f][c] >= carton[f+1][c]:
            
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+1][c]=num_nuevo
        
        elif carton[f][c] and carton[f+1][c] == False and carton[f+2][c]:
        
            while carton[f][c] >= carton[f+2][c]:
        
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+2][c]=num_nuevo
        
        elif carton[f][c] == False and carton[f+1][c] and carton[f+2][c]:
        
            while carton[f+1][c] >= carton[f+2][c]:
        
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+1][c]=num_nuevo
                num_nuevo=random.randint(1,9) + (c*10)
                carton[f+2][c]=num_nuevo
    
    carton_ = carton[0] + carton[1] + carton[2]

    return carton_

# cantidad = int(input("Ingrese la cantidad de cartones a generar: "))

def cartones(cantidad):
  
    cantidad_list = []
    i = 0
    while i < cantidad:
        carton_generado = carton()
        if not carton_generado in cantidad_list:
            cantidad_list.append(carton_generado)
            i += 1
    return cantidad_list



# i=0
# for item in cartones(cantidad):
#     i+=1
#     print(f"Carton { i } Fila 1: {item[:9]}")
#     print(f"         Fila 2: {item[9:18]}")
#     print(f"         Fila 3: {item[18:27]}")

