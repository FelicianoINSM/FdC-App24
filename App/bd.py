import sqlite3
from datetime import datetime

def obtener_nombre_dia(fecha):
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    numero_dia = fecha.weekday()
    return nombres_dias[numero_dia]
# Función para conectar a la base de datos
def conectar_base_datos():
    try:
        conn = sqlite3.connect('historial.db')
        return conn
    except sqlite3.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Configuración de la base de datos SQLite
def configurar_base_datos():
    conn = conectar_base_datos()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS historial (
                    id INTEGER PRIMARY KEY,
                    descripcion TEXT,
                    fecha TEXT,
                    hora TEXT
                )
            ''')
            conn.commit()
            print("Base de datos configurada correctamente")
        except sqlite3.Error as e:
            print("Error al configurar la base de datos:", e)
        finally:
            conn.close()

# Funciones para operaciones CRUD en la base de datos SQLite
def agregar_entrada(descripcion, fecha, hora):
    conn = conectar_base_datos()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO historial (descripcion, fecha, hora) VALUES (?, ?, ?)', (descripcion, fecha, hora))
            conn.commit()
            print("Entrada agregada correctamente")
        except sqlite3.Error as e:
            print("Error al agregar entrada:", e)
        finally:
            conn.close()

def obtener_ultimas_entradas(num_entradas=6):
    conn = conectar_base_datos()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM historial ORDER BY id DESC LIMIT ?', (num_entradas,))
            entradas = cursor.fetchall()
            return entradas
        except sqlite3.Error as e:
            print("Error al obtener últimas entradas:", e)
        finally:
            conn.close()

# Configurar la base de datos antes de agregar una entrada
configurar_base_datos()

# Ejemplo de agregar una entrada al historial
fecha = datetime.now().strftime('%Y-%m-%d')
hora = datetime.now().strftime('%H:%M:%S')
nombre_dia = obtener_nombre_dia(datetime.now())
descripcion = nombre_dia
agregar_entrada(descripcion, fecha, hora)