from datetime import datetime
import sqlite3 as sql
class DB:
    def start(self):
        con = sql.connect('./server/server.db')
        cur = con.cursor()
        return con, cur
    
    def create_tbls(self):
        con, cur = self.start()
        cur.execute('''CREATE TABLE IF NOT EXISTS riegos (
                    id INTEGER PRIMARY KEY,
                    fecha TEXT,
                    inicio TEXT,
                    final TEXT,
                    agua INT,
                    humedad INT
        )''')
        con.commit()
        cur.close()
    
    # DATA = {"fecha":datetime.date(FECHA).strftime('%Y-%m-%d'), "inicio":"22:30", "final":"23:00", "agua":30, "humedad":78}
    def add_entry(self, data):
        con, cur = self.start()

        values = (data['fecha'], data['inicio'], data['final'], data['agua'], data['humedad'])
        cur.execute("INSERT INTO riegos (fecha, inicio, final, agua, humedad) VALUES (?, ?, ?, ?, ?)", values)
        
        con.commit()
        cur.close()

    def get_all(self):
        con, cur = self.start()
        cur.execute("SELECT fecha, inicio, final, agua, humedad FROM riegos")
        data = cur.fetchall()
        cur.close()
        return data

if __name__ == "__main__":
    DB().create_tbls()
    