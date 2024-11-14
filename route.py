from flask import Flask, render_template, jsonify
from flask_cors import CORS

# import controller
from controller.algorithm_function import algorithm_function

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# Contoh Rute generate viginere
@app.route("/viginere", methods=['GET'])
def generate_viginere():
    return algorithm_function().viginere()



if __name__ == "__main__":
    app.run(debug=True)
