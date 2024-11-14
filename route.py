from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

# import controller
from controller.algorithm_function import algorithm_function

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# Contoh Rute generate viginere
@app.route("/viginere", methods=['POST'])
def generate_viginere():
    data = request.get_json()
    key_data = str(data.get('key'))
    return algorithm_function().viginere(key_data)

@app.route("/caesarcipher", methods=['POST'])
def generate_caesar_cipher():
    data = request.get_json()
    shift = int(data.get('shift'))  # Mengambil nilai shift dari data JSON
    return algorithm_function().caesar_cipher(shift)




if __name__ == "__main__":
    app.run(debug=True)
