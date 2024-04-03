from connection import Connect
from kivy.uix.screenmanager import Screen
import os
import configparser


import kivy
kivy.require('2.3.0')

from kivy.config import Config
Config.set('graphics', 'width', '600')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class Home(Screen):
    pass

class Menu(Screen):
    pass
        
class Configuracion(Screen):
    def save_server_address(self):
        server_address = self.ids.server_address_input.text.strip()
        
        if not server_address:
            print("Error: Por favor, ingrese una dirección de servidor válida.")
            return

        config = configparser.ConfigParser()

        config['Servidor'] = {'direccion': server_address}

        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            config_file_path = os.path.join(dir_path, 'configuracion.cfg')

            with open(config_file_path, 'w') as configfile:
                config.write(configfile)

            print("Dirección del servidor guardada:", server_address)
        except Exception as e:
            print("Error al escribir en el archivo de configuración:", e)

        print("Dirección del servidor guardada:", server_address)

class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class Riego(App):

    def build(self):
        return kv

if __name__ == '__main__':
    riegoApp = Riego()
    riegoApp.run()