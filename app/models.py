from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return usuario.query.get(user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    def json(self):
        return{
            'id':self.id,
            'nome':self.nome,
            'email':self.email,
            'senha':self.senha
        } 

class anuncios(db.Model):
    __tablename__ = "anuncios"
    id = db.Column(db.Integer, primary_key=True)    
    titulo = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    links = db.Column(db.String(255), nullable=False)
    plataforma = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
class admins(db.Model, UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  
