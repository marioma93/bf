from flask import Flask, render_template, request
from app import app, pages

#app2 = Flask(__name__)

@app2.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        name = None
    if request.method == "POST":
        name = request.form.get("name")
    bf = False
    for n in ['varo', 'Varo', 'VARO', 'Alvaro', 'Álvaro', 'alvaro', 'álvaro',
              'ALVARO', 'ÁLVARO', 'varito', 'Varito', 'apm14']:
        if n == name:
            bf = True
    return render_template("index.html", name=name, bf=bf)


