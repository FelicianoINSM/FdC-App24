from flask.views import MethodView
from flask import request, make_response, jsonify, render_template

class Home(MethodView):
    def get(self):
        return render_template('index.html')
    # def post(self):
    #     data = request.get_json()
    #     if data["msg"]:
    #         return data["msg"]
    #     else:
    #         return None