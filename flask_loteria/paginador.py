

def paginador(cantidad_paginas, pagina=1 ):

    lista_numeros = []
    for numeros_paginas in range(1, cantidad_paginas+1):
        lista_numeros.append(numeros_paginas)

    if pagina <= 5:
        lista_paginas = lista_numeros[  : 9 ]

    if pagina > 5:
        lista_paginas = lista_numeros[ pagina - 5 : pagina + 4 ]

    if pagina >= len(lista_numeros) - 4:
        lista_paginas = lista_numeros[ (len(lista_numeros) - 4) - 5 : len(lista_numeros) ]

    if len(lista_numeros) <= 9:
        lista_paginas = lista_numeros[ :len(lista_numeros) ]
        
    print(lista_paginas)
    return lista_paginas
    









