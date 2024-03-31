from flask.views import MethodView
from flask import request, jsonify, render_template
from datetime import datetime

class Home(MethodView):
    def get(self):
        return render_template('index.html')

class Daily(MethodView):
    def get(self):
        # GET FROM sensor.py
        data = {
            "temp": 32,
            "f_hum": 20,
            "e_hum": 45,
            "last": datetime.now()
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
    # GET
    pass

class Timer(MethodView):
    # GET, POST
    pass