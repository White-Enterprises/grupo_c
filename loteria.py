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
            num=random.randint(1,9) + (posicion*10)
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
        if carton[f][c] and carton[f+1][c] and carton[f+2][c]: # 3 NUMEROS 3 POSICIONES TRUE 
        
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
    return carton

pp(carton())


