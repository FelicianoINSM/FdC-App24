
import requests
from connection import Connect
from datetime import datetime


import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '650')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

class Home(Screen):
    switch_button = ObjectProperty(None)
    temp = ObjectProperty(None)
    env_humidity = ObjectProperty(None)
    humidity = ObjectProperty(None)
    last_time = ObjectProperty(None)

    def switch_button_pressed(self):
        switch_button = self.ids.switch_button
        if switch_button.text == "Encender":
            switch_button.text = "Apagar"
        else:
            switch_button.text = "Encender"
    

class Menu(Screen):
    pass
        
class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class Riego(App):
    def build(self):
            return kv
    def on_start(self):
            data = requests.get("http://127.0.0.1:5000/v1/daily").json()
            temperatura = str(data["temp"])
            humedad_ambiente = str(data["e_hum"])
            humedad_suelo = str(data["f_hum"])
            ultimo_riego = data["last"]
          
            home_screen = self.root.get_screen('home')
            home_screen.temp.text = temperatura +"°"
            home_screen.env_humidity.text = humedad_ambiente + "%"
            home_screen.humidity.text = humedad_suelo + "%"
            home_screen.last_time.text = ultimo_riego + "hs"

    

    

if __name__ == '__main__':
    riegoApp = Riego()
    riegoApp.run()