#criando a estrutura do banco de dados
from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin #usado para passar os parametros de segurança e login

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True) #unique = email precisa ser único
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True) 
    #Foto está referenciando a classe foto e o backref é uma referencia ao usuario como uma relação na classe foto. 
    #Já cria aqui para não precisar criar a relação na outra classe.

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)