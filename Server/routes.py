from flask.views import MethodView
from flask import request, jsonify, render_template
from datetime import datetime
from utils.db import DB

class Home(MethodView):
    def get(self):
        return render_template('index.html')

class Daily(MethodView):
    def get(self):
        data = {
            "temp": 32,
            "f_hum": 20,
            "e_hum": 45,
            "last": datetime.now().strftime("%d,%m,%Y")
        }
        return jsonify(data)
    
class Status(MethodView):
    def get(self):
        return jsonify({
            "aspersores":True
        })
    def post(self):
        data = request.json
        print(data)
        return jsonify("Receieved")
    
class History(MethodView):
    def get(self):
        data = DB().get_all()
        return jsonify(data)

class Time(MethodView):
    def get(self):
        return jsonify({"days":["Lunes", "Martes", "Sabado"], "start":"14:30", "end":"16:30"})
    def post(self):
        data = request.json
        print(data)
        return jsonify({"message":"Programación modificada con éxito"})
    
