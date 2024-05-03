from connection import Connect

import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.clock import Clock



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
        # Conectar a la base de datos
        conn = sqlite3.connect("historial.db")
        cursor = conn.cursor()
        
        # Obtener las últimas 6 entradas del historial
        cursor.execute("SELECT * FROM historial ORDER BY id DESC LIMIT 6")
        historial = cursor.fetchall()
        
        conn.close()
        
        # Limpiar el GridLayout antes de agregar nuevas entradas
        historial_grid = self.ids["hi"]
        historial_grid.clear_widgets()
        
        # Agregar las entradas del historial al GridLayout
        for entrada in historial:
            descripcion, fecha, hora, final, litros, humedad = entrada[1], entrada[2], entrada[3], entrada[4], entrada[5], entrada[6]
            historial_grid.add_widget(Label(text=descripcion, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=fecha, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=hora, font_size=12, color=(0.53, 0, 0.95, 0.8)))  
            historial_grid.add_widget(Label(text=final, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=litros, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=humedad, font_size=12, color=(0.53, 0, 0.95, 0.8)))

class Home(Screen):
    pass

class Vermas(Screen):
    def __init__(self, **kwargs):
        super(Vermas, self).__init__(**kwargs)
        Clock.schedule_once(self.cargar_historial)

    def cargar_historial(self, dt):
        # Conectar a la base de datos
        conn = sqlite3.connect("historial.db")
        cursor = conn.cursor()
        
        # Obtener las últimas 6 entradas del historial
        cursor.execute("SELECT * FROM historial ORDER BY id DESC")
        historial = cursor.fetchall()
        
        conn.close()
        
        # Limpiar el GridLayout antes de agregar nuevas entradas
        historial_grid = self.ids["hi"]
        historial_grid.clear_widgets()
        
        # Agregar las entradas del historial al GridLayout
        for entrada in historial:
            descripcion, fecha, hora, final, litros, humedad = entrada[1], entrada[2], entrada[3], entrada[4], entrada[5], entrada[6]
            historial_grid.add_widget(Label(text=descripcion, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=fecha, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=hora, font_size=12, color=(0.53, 0, 0.95, 0.8)))  
            historial_grid.add_widget(Label(text=final, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=litros, font_size=12, color=(0.53, 0, 0.95, 0.8)))
            historial_grid.add_widget(Label(text=humedad, font_size=12, color=(0.53, 0, 0.95, 0.8)))

class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')


class RiegoApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    RiegoApp().run()
        