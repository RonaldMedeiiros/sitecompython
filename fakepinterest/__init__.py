from flask import Flask

app = Flask(__name__)

from fakepinterest import routes #importações dos arquivos após o app. para não dar conflito de quando o routes precisar do app