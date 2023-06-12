from loteria import carton

cartones_txt = open("cartones.txt", "a" , encoding="utf-8")

cantidad = int(input("Ingrese la cantidad de cartones a generar: "))

i = 0

while i < cantidad:
    existe = 0
    cart = carton()
    carton_str = str(cart)
    caracter_remplazo = "[]"
    for remplazo in caracter_remplazo:
        carton_str = carton_str.replace(remplazo, '')

    with open("cartones.txt", "r", encoding="utf-8") as cartones:

        for fila in cartones:
            if carton_str == fila.strip():
                existe += 1 

        if existe == 0:
            cartones_txt.write(f"{carton_str}\n")
            i+=1
cartones_txt.close()

cartones_txt = open("cartones.txt", "r", encoding="utf-8")

for item in cartones_txt:
    print(item)

cartones_txt.close()

