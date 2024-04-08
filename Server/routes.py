from flask.views import MethodView
from flask import request, make_response, jsonify
from utils.esp32 import esp32

class Home(MethodView):
    def get(self):
        return esp32().info()
    def post(self):
        data = request.get_json()
        if data["msg"]:
            return data["msg"]
        else:
            return None