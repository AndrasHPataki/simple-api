from flask import jsonify, request
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
import sys
sys.path.insert(0, 'app_structure/database')
from models import User
from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
import datetime
auth = HTTPBasicAuth()



class MainAuth():
    def __init__(self):
        self.username = request.json.get('username')
        self.password = request.json.get('password')


@auth.verify_password
def verify_password(username,password):
    usuario_existe = User.query.filter_by(username=username).first()
    if  usuario_existe and check_password_hash(usuario_existe.password, password):
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(usuario_existe.username), expires_delta=expires)
        return access_token
    

class Secure(Resource):
    @jwt_required
    def get(self):
        user_name = get_jwt_identity()
        return  jsonify({"message": "It is a Protected route", "current_user": user_name})


class Login(Resource):
    def get(self):
        return jsonify({"message": "Login GET"})

    @auth.login_required
    def post(self):
        return jsonify({"access-token": auth.current_user()})

class SignUp(Resource):
    def get(self):
        return jsonify({"message": "SignUp GET"})
    def post(self):
        main_user  = MainAuth()
        if main_user.username and main_user.password:
            usuario_existe = User.query.filter_by(username=main_user.username).first()
            if usuario_existe:
                return jsonify({"message": "user already signup"})
            else:
                try:
                    username = str(main_user.username)
                    password = str(main_user.password) 
                    novo_usuario = User(username=username,password=generate_password_hash(password, method='sha256'))
                    db.session.add(novo_usuario)
                    db.session.commit()
                except:
                    return jsonify({"message": "Something Wrong!"})
                
        return jsonify({"username": main_user.username, "password": "Its Encrypted!"})
   
