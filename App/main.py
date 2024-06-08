from connection import Connect

import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests 
from connection import Connect
import requests
from datetime import *
import locale
class Home(Screen):
    pass

class Menu(Screen):
    pass

import sqlite3

class Historial(Screen):
    def __init__(self, **kwargs):
        super(Historial, self).__init__(**kwargs)
        Clock.schedule_once(self.cargar_historial)

    def cargar_historial(self, dt):
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        response = requests.get("http://fdcyt24.ddns.net:5000/v1/history")
        data = response.json()[:5]  # Obtener las primeras seis entradas
        grid = self.ids.hi
        grid.clear_widgets()

        # Procesar cada entrada y agregar los datos a las columnas
        for entry in data:
            fecha = entry[0]
            nombre_dia = self.obtener_nombre_dia(fecha).capitalize()
            grid.add_widget(Label(text=nombre_dia, font_size=12, color=(0.53, 0, 0.95, 0.8)))  # Agregar nombre del día
            
            # Agregar los otros elementos de la entrada a las columnas restantes
            for item in entry[0:]:
                grid.add_widget(Label(text=str(item), font_size=12, color=(0.53, 0, 0.95, 0.8)))

    def obtener_nombre_dia(self, fecha_str):
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
        nombre_dia = fecha_obj.strftime("%A")
        return nombre_dia

class Home(Screen):
    pass

class Vermas(Screen):
    def __init__(self, **kwargs):
        super(Vermas, self).__init__(**kwargs)
        Clock.schedule_once(self.cargar_historial)

    def cargar_historial(self, dt):
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        response = requests.get("http://fdcyt24.ddns.net:5000/v1/history")
        data = response.json()  # Obtener las primeras seis entradas
        grid = self.ids.hi
        grid.clear_widgets()

        # Procesar cada entrada y agregar los datos a las columnas
        for entry in data:
            fecha = entry[0]
            nombre_dia = self.obtener_nombre_dia(fecha).capitalize()
            grid.add_widget(Label(text=nombre_dia, font_size=12, color=(0.53, 0, 0.95, 0.8)))  # Agregar nombre del día
            
            # Agregar los otros elementos de la entrada a las columnas restantes
            for item in entry[0:]:
                grid.add_widget(Label(text=str(item), font_size=12, color=(0.53, 0, 0.95, 0.8)))

    def obtener_nombre_dia(self, fecha_str):
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
        nombre_dia = fecha_obj.strftime("%A")
        return nombre_dia

class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')


class RiegoApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    RiegoApp().run()
        