from flask import Flask, render_template
from flask_cors import CORS

# import controller
from controller.algorithm_function_chapter_1 import algorithm_function_chapter_1
from controller.algorithm_function_chapter_2 import algorithm_function_chapter_2
from controller.algorithm_function_chapter_3 import algorithm_function_chapter_3
from controller.algorithm_function_chapter_4 import algorithm_function_chapter_4
from controller.algorithm_function_chapter_5 import algorithm_function_chapter_5

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

@app.route("/chapterlima", methods=['POST'])
def chapter_lima():
    return render_template("chapter_lima.html")


# Generate for Chapter 1
@app.route("/caesarcipherchapterone", methods=['POST'])
def generate_chapterone():
    return algorithm_function_chapter_1().caesar_cipher()

# Generate for Chapter 2
@app.route("/viginerechaptertwo", methods=['POST'])
def generate_chaptertwo():
    return algorithm_function_chapter_2().viginere()

# Generate for Chapter 3
@app.route("/caesarcipherchapterthree", methods=['POST'])
def generate_chapterthree():
    return algorithm_function_chapter_3().caesar_cipher()

# Generate for Chapter 4
@app.route("/viginerechapterfour", methods=['POST'])
def generate_chapterfour():
    return algorithm_function_chapter_4().viginere()

# Generate for Chapter 5
@app.route("/caesarcipherchapterfive", methods=['POST'])
def generate_chapterfive():
    return algorithm_function_chapter_5().caesar_cipher()




if __name__ == "__main__":
    app.run(debug=True)
