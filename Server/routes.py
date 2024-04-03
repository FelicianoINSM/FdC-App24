from functools import wraps
from flask.views import MethodView
from flask import request, make_response, jsonify, render_template, redirect, url_for, Response
from auth import auth_required

class Home(MethodView):
    def get(self):
        return 'Hello World!'
    def post(self):
        data = request.get_json()
        if data["msg"]:
            return data["msg"]
        else:
            return None
        

USERS = {
    "admin": "password123"
}
def check_auth(username, password):
    return USERS.get(username) == password

def authenticate():
    return Response(
        'Ingrese las credenciales.', 
        401, 
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

class Admin(MethodView):
    def get(self):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        
       
        return render_template('admin.html')
