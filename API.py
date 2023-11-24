from flask import Flask, jsonify, request

app = Flask(__name__)

from maestros import maestros

@app.route("/ping")
def ping():
    return jsonify({"message": "Bievenidos"})

@app.route('/maestros')
def getMaestros():
    return  jsonify(maestros)

#Funcion Para Buscar Maestros
@app.route('/maestros/<string:maestro_name>')
def getMaestro(maestro_name):
    maestroFound = [maestro for maestro in maestros if maestro['name'] == maestro_name]
    if (len(maestroFound)>0):
        return jsonify({"maestro": maestroFound[0]})
    return jsonify({"Mensaje": "Maestro No Encontrado"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)