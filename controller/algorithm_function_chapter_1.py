from flask import jsonify
import random

class algorithm_function():
    # Database kalimat sederhana
    sentences = [
        "JETHRO",
        "KENANG",
        "KECE",
        "RICHARD",
    ]

    kunci = [
        {"one": 1},
        {"dua": 2},
        {"tiga": 3},
        {"empat": 4},
        {"five": 5},
        {"enam": 6},
        {"seven": 7},
        {"eight": 8},
        {"nine": 9},
        {"ten": 10}
    ]

    def viginere(self):
        text_decrypted = random.choice(self.sentences)
        key_dict = random.choice(self.kunci)
        key = list(key_dict.keys())[0]
        
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        text_as_int = [ord(i) for i in text_decrypted]

        encrypted_text = ""
        for i in range(len(text_as_int)):
            if text_decrypted[i].isalpha():  # Hanya mengenkripsi huruf
                offset = 65 if text_decrypted[i].isupper() else 97
                encrypted_char = chr((text_as_int[i] + key_as_int[i % key_length] - 2 * offset) % 26 + offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += text_decrypted[i]  # Biarkan karakter non-huruf tetap sama

        output = {
            'teks_enkripsi': encrypted_text,
            'teks_dekripsi': text_decrypted,
            'kunci': key
        }
    
        return jsonify(output)

    def caesar_cipher(self):
        text_decrypted = random.choice(self.sentences)
        shift_dict = random.choice(self.kunci)
        shift = list(shift_dict.values())[0]
        shift_key = list(shift_dict.keys())[0]
        
        encrypted_text = ""
        for char in text_decrypted:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        
        output = {
            'teks_enkripsi': encrypted_text,
            'teks_dekripsi': text_decrypted,
            'kunci': shift_key
        }
        return jsonify(output)