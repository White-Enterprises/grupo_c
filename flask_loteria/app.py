from flask import Flask, request, redirect
from flask import render_template
import json
import os
import math

from generacion_json2 import generar_json
from cant_cartones import carton_por_pagina
from paginador import paginador


path_loteria = "data/cartones.json"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("index.html")
    

@app.route("/cartones", methods=['POST'])
@app.route('/cartones/<int:pagina>', methods=['GET', 'POST'])
def vista_cartones(pagina=1):
    path_json = os.path.exists(path_loteria)
    if request.method == 'POST':
        if "valor" in request.form.keys():
            cantidad = int(request.form.get("valor"))
            generar_json(cantidad)
        if "valor_pag" in request.form.keys():
            pagina = int(request.form["valor_pag"])
        return redirect(f'/cartones/{pagina}') 

    if path_json:
        archivo = open(path_loteria, "r")
        datos_json = json.load(archivo)
        archivo.close()
        cantidad_paginas = math.ceil(len(datos_json)/3)
        datos_json = carton_por_pagina(pagina, datos_json)
        paginas = paginador(cantidad_paginas, pagina )
        return render_template ("cartones.html", datos_json = datos_json, path_json = path_json, cantidad_paginas=cantidad_paginas, paginas=paginas)
    
    else:
        return render_template ("cartones.html", path_json = path_json)




if __name__ == '__main__':
    app.run(debug=True)
