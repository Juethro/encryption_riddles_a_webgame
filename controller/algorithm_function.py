from flask import jsonify
import random

class algorithm_function():
    # Database kalimat sederhana
    sentences = [
        "Langit biru di pagi hari",
        "Matahari terbenam indah sekali",
        "Aku suka bermain musik",
        "Belajar adalah kunci sukses",
        "Ayo semangat belajar hari ini",
        "Hidup sehat dengan olahraga",
        "Pikiran tenang hidup nyaman",
        "Selalu berpikir positif",
        "Buku adalah jendela dunia",
        "Langkah kecil menuju mimpi",
        "Hujan turun sangat deras",
        "Kopi panas di pagi hari",
        "Warna-warni bunga di taman",
        "Es krim favoritku rasa coklat",
        "Berani mencoba hal baru",
        "Mendaki gunung sangat seru",
        "Cinta damai untuk semua",
        "Senyum membawa kebahagiaan",
        "Air laut terasa asin",
        "Pagi hari udara sejuk sekali",
        "Rindu suasana kampung halaman",
        "Menonton film adalah hiburan",
        "Makan siang bersama teman",
        "Hewan peliharaan sangat lucu",
        "Liburan ke pantai menyenangkan",
        "Bersyukur setiap hari",
        "Musik bisa menenangkan hati",
        "Aku suka belajar teknologi",
        "Taman kota penuh bunga indah",
        "Selalu belajar dari kesalahan"
    ]

    def viginere(self):
        teks_enkripsi = "hehe"
        teks_dekripsi = "dekripso"

        output = {
            'teks_enkripsi': teks_enkripsi,
            'teks_dekripsi': teks_dekripsi
        }
    
        return jsonify(output)

    def caesar_cipher(self, shift):
        text_decrypted = random.choice(self.sentences)
        
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
            'teks_dekripsi': text_decrypted
        }
        return jsonify(output)
