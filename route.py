from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

# import controller
from controller.algorithm_function import algorithm_function

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/chaptersatu", methods=['POST'])
def chapter_satu():
    return render_template("chapter_satu.html")

@app.route("/chapterdua", methods=['POST'])
def chapter_dua():
    return render_template("chapter_dua.html")

@app.route("/chaptertiga", methods=['POST'])
def chapter_tiga():
    return render_template("chapter_tiga.html")

@app.route("/chapterempat", methods=['POST'])
def chapter_empat():
    return render_template("chapter_empat.html")


# Contoh Rute generate viginere
@app.route("/viginere", methods=['POST'])
def generate_viginere():
    # data = request.get_json()
    # key_data = str(data.get('key'))
    return algorithm_function().viginere()

@app.route("/caesarcipher", methods=['POST'])
def generate_caesar_cipher():
    # data = request.get_json()
    # shift = int(data.get('shift'))  # Mengambil nilai shift dari data JSON
    return algorithm_function().caesar_cipher()




if __name__ == "__main__":
    app.run(debug=True)
