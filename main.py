from flask import Flask

app = Flask(__name__)

@app.route("/")

def homepage():
    return "Meu primeiro site no ar"

if __name__ == "__main__": #para executar esse arquivo só quando ele for chamado e não importado, se importar não vai rodar esse if
    app.run(debug=True)