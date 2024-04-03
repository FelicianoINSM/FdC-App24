from flask import Flask
from routes import Home, Daily, Status, History, Time

class Listener:
    def __init__(self):
        self.app = Flask(__name__)

    def rules(self):
        self.app.add_url_rule('/', view_func=Home.as_view('home'))
        self.app.add_url_rule('/v1/daily', view_func=Daily.as_view('daily'))
        self.app.add_url_rule('/v1/status', view_func=Status.as_view('status'))
        self.app.add_url_rule('/v1/history', view_func=History.as_view('history'))
        self.app.add_url_rule('/v1/time', view_func=Time.as_view('time'))
    
    def run(self):
        self.rules()
        self.app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == '__main__':
    Listener().run()