# encryption_riddles_a_webgame
A Riddles Web Game, made of python with flask.

# Folder Structures
```
controller/
```
Berisi fungsi atau algoritma dalam web, akan dipanggil di route.py

```
templates/
```
Berisi file UI seperti HTML

`static/`
Berisi file statis seperti CSS dan Javascript serta aset web

# How To Setup
Note: Gunakan Python3.10

### Buat virtual environment
```bash
python3.10 -m venv env
```

### Aktifkan virtual environment (windows)
```bash
env/Scripts/activate
```

### Aktifkan virtual environment (linux)
```bash
source env/bin/activate
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Jalankan flask 
export terlebih dahulu
```bash
export FLASK_APP=route.py
```

jalankan flask
```bash
python route.py
```

jalankan flask dengan debug mode
```bash
flask run --debug
```
