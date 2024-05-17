from flask_restful import Resource, reqparse
from app.models import usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from blacklist import BLACKLIST
from app import db

class User_modelo(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('senha')

def get(self):
    return {'Usuarios':[usuari.json() for usuari in usuario.query.all()]}

def post(self):
    dados = User_modelo.argumentos.parse_args()
    users = usuario(**dados)
    db.session.add(users)
    db.session.commit()
    return users.json(), 201

class Users_modelo(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('senha')

def get(self,id):
    users = usuario.query.filter_by(id=id).first()
    if users:
        return users.json
    return {'message': 'Usuario Inexistente'}, 404

def put(self, id):
    dados = Users_modelo.argumentos.parse_args()
    users = usuario(**dados)
    user_encontrado = usuario.query.filter_by(id=id).first()
    if user_encontrado:
        user_encontrado.query.filter_by(id=id).update({**dados})
        db.session.commit()
        return user_encontrado.json(),200
    db.session.add(users)
    db.session.commit()
    return users.json(),201

def delete(self,id):
    users = usuario.query.filter_by(id=id).first()
    if users:
        db.session.delete(users)
        db.session.commit()
        return {'message': 'Usuario Excluido!'}
    return {'message': 'Usuario Inexistente'}, 404

