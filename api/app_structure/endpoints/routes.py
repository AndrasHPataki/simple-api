from flask_restful import Resource, Api
from flask import Blueprint
import sys
main = Blueprint('main', __name__)

def config(funcao):
    def wrapper():
        sys.path.insert(0, 'app_structure/methods')
        from resource import SignUp,Login,Secure
        api = funcao()
        api.add_resource(SignUp, '/api/v1/signup')
        api.add_resource(Login, '/api/v1/login')
        api.add_resource(Secure, '/api/v1/secure')
    return wrapper

@config
def router():
    api = Api(main)
    return api

if __name__ == 'app_structure.endpoints.routes':
    router()