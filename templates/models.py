from main import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column( database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_de_perfil = database.Column(database.String, default='default.jpg')
    post = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado!')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False)
