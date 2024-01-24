from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager #instalar os pacotes "pip install flask-login flask-bcrypt" que são pacotes para gerenciar login e segurança
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "5b0426232c3e36bf0c6efe6b1cc82256" #usar o gerarsenha.py

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes #importações dos arquivos após o app. para não dar conflito de quando o routes precisar do app