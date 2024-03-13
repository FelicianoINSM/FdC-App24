
from connection import Connect

import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.switch import Switch

class MySwitch(Switch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(active=self.hi)

    def hi(self, _, state):
        Connect.ping()

class Home(Screen):
    pass

class Menu(Screen):
    pass
        
class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class Riego(App):

    def build(self):
        return kv

if __name__ == '__main__':
    riegoApp = Riego()
    riegoApp.run()