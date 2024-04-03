from functools import wraps

from flask import make_response, request, current_app

def auth_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth = request.authorization
        if auth and auth.username == current_app.config["SITE_USER"] and auth.password == "pass":
            return f(*args, **kwargs)
        return make_response("<h1>Acceso denegado!</h1>", 401, {'WWW-Auhtenticate': 'Basic realm="Login Required!"'})
    
    return decorated

