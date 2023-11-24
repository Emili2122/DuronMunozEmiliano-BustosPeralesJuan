from flask import Flask, jsonify, request

app = Flask(__name__)

from maestros import maestros

@app.route("/ping")
def ping():
    return jsonify({"message": "Bievenidos"})

@app.route('/maestros')
def getMaestros():
    return  jsonify(maestros)

if __name__ == "__main__":
    app.run(debug=True, port=5000)