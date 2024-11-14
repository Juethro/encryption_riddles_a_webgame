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

    import random

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

# Fungsi untuk mengenkripsi menggunakan Caesar Cipher
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi menggunakan Caesar Cipher
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Memilih kalimat acak dan melakukan enkripsi
random_sentence = random.choice(sentences)
shift = random.randint(1, 25)  # Pilih pergeseran acak antara 1 dan 25
encrypted_sentence = caesar_cipher(random_sentence, shift)

# Menampilkan hasil
print("Kalimat terenkripsi untuk ditebak:")
print(encrypted_sentence)
print("\nJumlah pergeseran:", shift)

# Opsi untuk mendekripsi
user_input = input("Apakah Anda ingin melihat kalimat asli? (ya/tidak): ")
if user_input.lower() == "ya":
    decrypted_sentence = caesar_decipher(encrypted_sentence, shift)
    print("Kalimat asli:", decrypted_sentence)
else:
    print("Silakan coba tebak kalimat aslinya!")
