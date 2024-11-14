from flask import jsonify

class algorithm_function():

    def viginere(self):
        teks_enkripsi = "hehe"
        teks_dekripsi = "dekripso"

        output = {
            'teks_enkripsi': teks_enkripsi,
            'teks_dekripsi': teks_dekripsi
        }

        return jsonify(output)
    
    