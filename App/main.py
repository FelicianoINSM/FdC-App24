
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


class MySwitch(Switch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(active=self.hi)

    def hi(self, _, state):
        Connect.ping()

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
    start_day_spinner = ObjectProperty(None)
  
    

    def save_schedule(self):
        start_hour = self.start_hour_spinner.text
        start_minute = self.start_minute_spinner.text
        end_hour = self.end_hour_spinner.text
        end_minute = self.end_minute_spinner.text
        start_day = self.start_day_spinner.text
        



  

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

