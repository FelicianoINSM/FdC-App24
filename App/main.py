import re
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
        # Expresión regular para capturar la dirección del servidor y el número de puerto
        regex = r'([a-zA-Z0-9.-]+):(\d+)'

        server_address = self.ids.server_address_input.text.strip()

        if not server_address:
            print("Error: Por favor, ingrese una dirección de servidor válida.")
            return

        # Verificar si la dirección del servidor coincide con la expresión regular
        match = re.match(regex, server_address)
        if not match:
            print("Error: La dirección del servidor debe tener el formato 'direccion:puerto'.")
            return

        # Extraer la dirección del servidor y el número de puerto del grupo de coincidencia
        server_address = match.group(1)
        port_number = match.group(2)

        config = configparser.ConfigParser()

        config['Servidor'] = {'direccion': server_address,
                              'puerto': port_number}

        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            config_file_path = os.path.join(dir_path, 'configuracion.cfg')

            with open(config_file_path, 'w') as configfile:
                config.write(configfile)

            print("Dirección del servidor y número de puerto guardados:", server_address, ":", port_number)
        except Exception as e:
            print("Error al escribir en el archivo de configuración:", e)

        print("Dirección del servidor y número de puerto guardados:", server_address, ":", port_number)

class TabManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class Riego(App):

    def build(self):
        return kv

if __name__ == '__main__':
    riegoApp = Riego()
    riegoApp.run()