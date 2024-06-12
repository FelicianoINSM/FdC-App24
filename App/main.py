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
from kivy.uix.checkbox import CheckBox


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
    start_hour_spinner = ObjectProperty(None)
    start_minute_spinner = ObjectProperty(None)
    end_hour_spinner = ObjectProperty(None)
    end_minute_spinner = ObjectProperty(None)
    day_checkboxes = ObjectProperty(None)

    def on_enter(self):
        self.store = JsonStore(os.path.join(App.get_running_app().user_data_dir, 'schedule.json'))
        self.load_schedule()

    def load_schedule(self):
        if self.store.exists('schedule'):
            data = self.store.get('schedule')
            self.ids.start_hour_spinner.text = data.get("start_hour", "00")
            self.ids.start_minute_spinner.text = data.get("start_minute", "00")
            self.ids.end_hour_spinner.text = data.get("end_hour", "00")
            self.ids.end_minute_spinner.text = data.get("end_minute", "00")
            days = data.get("days", [])
            for day in days:
                if day == "Lunes":
                    self.ids.day_monday.active = True
                elif day == "Martes":
                    self.ids.day_tuesday.active = True
                elif day == "Miércoles":
                    self.ids.day_wednesday.active = True
                elif day == "Jueves":
                    self.ids.day_thursday.active = True
                elif day == "Viernes":
                    self.ids.day_friday.active = True
                elif day == "Sábado":
                    self.ids.day_saturday.active = True
                elif day == "Domingo":
                    self.ids.day_sunday.active = True
        else:
            try:
                response = requests.get("http://192.168.120.99:5000/v1/time")
                if response.status_code == 200:
                    data = response.json()
                    self.ids.start_hour_spinner.text = data.get("start_hour", "00")
                    self.ids.start_minute_spinner.text = data.get("start_minute", "00")
                    self.ids.end_hour_spinner.text = data.get("end_hour", "00")
                    self.ids.end_minute_spinner.text = data.get("end_minute", "00")
                    days = data.get("days", [])
                    for day in days:
                        if day == "Lunes":
                            self.ids.day_monday.active = True
                        elif day == "Martes":
                            self.ids.day_tuesday.active = True
                        elif day == "Miércoles":
                            self.ids.day_wednesday.active = True
                        elif day == "Jueves":
                            self.ids.day_thursday.active = True
                        elif day == "Viernes":
                            self.ids.day_friday.active = True
                        elif day == "Sábado":
                            self.ids.day_saturday.active = True
                        elif day == "Domingo":
                            self.ids.day_sunday.active = True
                else:
                    print("Error al obtener la configuración del servidor")
            except Exception as e:
                print(f"Error al conectar con el servidor: {e}")

    def save_schedule(self):
        start_hour = self.ids.start_hour_spinner.text
        start_minute = self.ids.start_minute_spinner.text
        end_hour = self.ids.end_hour_spinner.text
        end_minute = self.ids.end_minute_spinner.text
        selected_days = []

        if self.ids.day_monday.active:
            selected_days.append("Lunes")
        if self.ids.day_tuesday.active:
            selected_days.append("Martes")
        if self.ids.day_wednesday.active:
            selected_days.append("Miércoles")
        if self.ids.day_thursday.active:
            selected_days.append("Jueves")
        if self.ids.day_friday.active:
            selected_days.append("Viernes")
        if self.ids.day_saturday.active:
            selected_days.append("Sábado")
        if self.ids.day_sunday.active:
            selected_days.append("Domingo")

        data = {
            "start_hour": start_hour,
            "start_minute": start_minute,
            "end_hour": end_hour,
            "end_minute": end_minute,
            "days": selected_days
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

