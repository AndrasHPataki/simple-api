from flask import Flask, Blueprint
from flask_restful import Api
#from flask_swagger import swagger
from .endpoints.routes import main,router
import sys
sys.path.insert(0, 'app_structure/database')
from db import run_db,db
from flask_jwt_extended import JWTManager

def create_app(config_file='settings.py'):
    app = Flask(__name__)   
    app.config.from_pyfile(config_file)
    app.register_blueprint(main)
    jwt = JWTManager(app)
    run_db(app)
    return app

