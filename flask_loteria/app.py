from flask import Flask, request, redirect
from flask import render_template
import json
import os

from generacion_json2 import generar_json


path_loteria = "data/cartones.json"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    path_json = os.path.exists(path_loteria)

    if request.method == 'POST':
        cantidad = int(request.form.get("valor"))
        generar_json(cantidad)
        return redirect('/')

    if path_json:
        archivo = open(path_loteria, "r")
        datos_json = json.load(archivo)
        archivo.close()
        return render_template ("index.html", datos_json = datos_json, path_json = path_json)
    
    else:
        return render_template ("index.html", path_json = path_json)


if __name__ == '__main__':
    app.run(debug=True)
