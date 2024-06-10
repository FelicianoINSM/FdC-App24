import requests
from connection import Connect
from kivy.uix.screenmanager import Screen

import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
import os 
import sqlite3 

class MySwitch(Switch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def hi(self, _, state):
        Connect.ping()

        response = requests.get("192.168.120.99")
        

        

class Home(Screen):
    pass

class Menu(Screen):
    def go_to_programar(self):
        self.manager.current = "programar"
        self.manager.transition.direction = "left"

    def go_to_historico(self):
        self.manager.current = "historico"
        self.manager.transition.direction = "left"

    def go_to_configuracion(self):
        self.manager.current = "configuracion"
        self.manager.transition.direction = "left"

class Programar(Screen):
    def on_enter(self):
        self.store = JsonStore(os.path.join(App.get_running_app().user_data_dir, 'schedule.json'))
        self.load_schedule()

    def load_schedule(self):
        if self.store.exists('schedule'):
            data = self.store.get('schedule')
            self.ids.start_hour_spinner.text = data.get("start_hour", "Seleccione la hora de inicio")
            self.ids.start_minute_spinner.text = data.get("start_minute", "Seleccione el minuto de inicio")
            self.ids.end_hour_spinner.text = data.get("end_hour", "Seleccione una hora de fin")
            self.ids.end_minute_spinner.text = data.get("end_minute", "Seleccione un minuto de fin")
            self.ids.start_day_spinner.text = data.get("day", "Selecciones un dia")
        else:
            try:
                response = requests.get("http://192.168.120.99:5000/v1/time")
                if response.status_code == 200:
                    data = response.json()
                    self.ids.start_hour_spinner.text = data.get("start_hour", "Seleccione la hora de inicio")
                    self.ids.start_minute_spinner.text = data.get("start_minute", "Seleccione el minuto de inicio")
                    self.ids.end_hour_spinner.text = data.get("end_hour", "Seleccione una hora de fin")
                    self.ids.end_minute_spinner.text = data.get("end_minute", "Seleccione un minuto de fin")
                    self.ids.start_day_spinner.text = data.get("day", "Selecciones un dia")
                else:
                    print("Error al obtener la configuración del servidor")
            except Exception as e:
                print(f"Error al conectar con el servidor: {e}")

    def save_schedule(self):
        start_hour = self.ids.start_hour_spinner.text
        start_minute = self.ids.start_minute_spinner.text
        end_hour = self.ids.end_hour_spinner.text
        end_minute = self.ids.end_minute_spinner.text
        day = self.ids.start_day_spinner.text

        data = {
            "start_hour": start_hour,
            "start_minute": start_minute,
            "end_hour": end_hour,
            "end_minute": end_minute,
            "day": day
        }

        self.store.put('schedule', **data)

        try:
            response = requests.post("http://192.168.120.99:5000/v1/time", json=data)
            if response.status_code == 200:
                print("Datos enviados correctamente")
            else:
                print("Error al enviar los datos")
        except Exception as e:
            print(f"Error al conectar con el servidor: {e}")


  

class Historico(Screen):
    pass

class Configuracion(Screen):
    pass
        
class TabManager(ScreenManager):
    pass



kv = Builder.load_file('main.kv')

class RiegoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Programar(name='programar'))
        return sm

if __name__ == '__main__':
    RiegoApp().run()

