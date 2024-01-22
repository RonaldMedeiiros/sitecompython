from flask import render_template, url_for
from fakepinterest import app


@app.route("/") #cada rota leva para uma página.
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)