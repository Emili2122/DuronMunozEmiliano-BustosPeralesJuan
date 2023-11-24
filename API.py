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

#Funcion Para Agregar Maestros
@app.route('/maestros', methods=['POST'])
def addMaestro():
    new_maestro = {
        "name": request.json['name'],
        "Materia": request.json['Materia'],
        "Numero de Empleado": request.json['Numero de empleado']
    }
    maestros.append(new_maestro)
    return jsonify({"mensaje": "Maestro agregado Satisfactoriamente", "maestros": maestros})

#EMILIANO TERMINA AQUI JAJA 

#Funcion Para Editar Maestros
@app.route('/maestros/<string:maestro_name>', methods=['PUT'])
def editmaestro(maestro_name):
    maestroFound = [maestro for maestro in maestros if maestro['name'] == maestro_name]
    if (len(maestroFound) >0):
        maestroFound[0]['name'] = request.json['name']
        maestroFound[0]['Materia'] = request.json['Materia']
        maestroFound[0]['Numero de empleado'] = request.json['Numero de empleado']
        return jsonify({
            "mensaje": "Maestro actualizado",
            "maestro": maestroFound[0]
        })
    return jsonify({"mensaje": "maestro no encontrado"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)