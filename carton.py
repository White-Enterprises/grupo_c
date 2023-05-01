import random
def x():
    i=0
    fila=[]
    while i < 9:
        fila.append(0)
        i+=1
    return fila

def position():
    fila=x()
    i=0
    while i < 5:
        posicion=random.randint(0,8)
        if posicion==0 and fila[posicion]==0:
            num=random.randint(1,9)
            fila[posicion]=num
            i+=1

        elif posicion==1 and fila[posicion]==0:
            num=random.randint(10,19)
            fila[posicion]=num
            i+=1

        elif posicion==2 and fila[posicion]==0:
            num=random.randint(20,29)
            fila[posicion]=num
            i+=1

        elif posicion==3 and fila[posicion]==0:
            num=random.randint(30,39)
            fila[posicion]=num
            i+=1

        elif posicion==4 and fila[posicion]==0:
            num=random.randint(40,49)
            fila[posicion]=num
            i+=1

        elif posicion==5 and fila[posicion]==0:
            num=random.randint(50,59)
            fila[posicion]=num
            i+=1

        elif posicion==6 and fila[posicion]==0:
            num=random.randint(60,69)
            fila[posicion]=num
            i+=1

        elif posicion==7 and fila[posicion]==0:
            num=random.randint(70,79)
            fila[posicion]=num
            i+=1

        elif posicion==8 and fila[posicion]==0:
            num=random.randint(80,89)
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
    while carton[0]==carton[1]:
        fila=position()
        carton[1]=fila
    while carton[0]==carton[2]:
        fila=position()
        carton[2]=fila
    while carton[1]==carton[2]:
        fila=position()
        carton[2]=fila
    return carton
print(carton())
