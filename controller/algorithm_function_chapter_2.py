from flask import jsonify
import random

class algorithm_function_chapter_2:
    # Database kalimat sederhana
    sentences = [
        "XJBLKP",
        "HRTWQZ",
        "MFJZNP",
        "VCKLYR",
        "QPSLDH",
        "ZBKJRW",
        "DFTLQM",
        "WRXHJC",
        "LPZQNV",
        "KGHLMP",
    ]

    kunci = [
        {"one": "ONE"},
        {"dua": "DUA"},
        {"tiga": "TIGA"},
        {"empat": "EMPAT"},
        {"five": "FIVE"},
        {"enam": "ENAM"},
        {"seven": "SEVEN"},
        {"eight": "EIGHT"},
        {"nine": "NINE"},
        {"ten": "TEN"}
    ]

    def viginere(self):
        # Memilih teks dan kunci secara acak
        text_decrypted = random.choice(self.sentences)
        key_dict = random.choice(self.kunci)
        key = list(key_dict.values())[0]  # Mengambil nilai kunci

        # Fungsi untuk menghasilkan key yang sesuai dengan panjang pesan
        def generate_key(msg, key):
            key = list(key)
            if len(msg) == len(key):
                return key
            else:
                for i in range(len(msg) - len(key)):
                    key.append(key[i % len(key)])
            return "".join(key)

        # Fungsi untuk mengenkripsi pesan menggunakan Vigenère
        def encrypt_vigenere(msg, key):
            encrypted_text = []
            key = generate_key(msg, key)
            for i in range(len(msg)):
                char = msg[i]
                if char.isupper():
                    encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
                elif char.islower():
                    encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
                else:
                    encrypted_char = char
                encrypted_text.append(encrypted_char)
            return "".join(encrypted_text)

        # Fungsi untuk mendekripsi pesan menggunakan Vigenère
        def decrypt_vigenere(msg, key):
            decrypted_text = []
            key = generate_key(msg, key)
            for i in range(len(msg)):
                char = msg[i]
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
                elif char.islower():
                    decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
                else:
                    decrypted_char = char
                decrypted_text.append(decrypted_char)
            return "".join(decrypted_text)

        # Encrypting and then decrypting the message
        encrypted_text = encrypt_vigenere(text_decrypted, key)
        decrypted_text = decrypt_vigenere(encrypted_text, key)

        output = {
            'teks_enkripsi': encrypted_text.upper(),
            'teks_dekripsi': decrypted_text.upper(),
            'kunci': key.upper()
        }
        return output