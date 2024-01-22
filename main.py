from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #cada rota leva para uma página.
def homepage():
    return render_template("homepage.html")

@app.route("/perfil")
def perfil():
    return "Perfil do Usuário"

if __name__ == "__main__": #para executar esse arquivo só quando ele for chamado e não importado, se importar não vai rodar esse if
    app.run(debug=True)