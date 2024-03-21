from flask import Flask
from routes import Home

class Listener:
    def __init__(self):
        self.app = Flask(__name__)

    def rules(self):
        self.app.add_url_rule('/', view_func=Home.as_view('home'))
    
    def run(self):
        self.rules()
        self.app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == '__main__':
    Listener().run()