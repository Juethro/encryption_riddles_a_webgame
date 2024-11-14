from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# Contoh Rute enkripsi viginere
@app.route("/enkripsi_viginere", methods=['POST'])
def enkripsi_viginere(text):
    pass

@app.route("/dekripsi_viginere", methods=['POST'])
def enkripsi_(text):
    pass



if __name__ == "__main__":
    app.run(debug=True)
