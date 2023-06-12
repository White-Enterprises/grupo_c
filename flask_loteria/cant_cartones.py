
def carton_por_pagina(pagina, datos_json):
    carton_desde = (pagina - 1) * 3
    carton_hasta = carton_desde + 3
    return datos_json[carton_desde:carton_hasta]
