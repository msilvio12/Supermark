import sqlite3


class SQLite():
    # Constructor
    def __init__(self, name: str):
        self.name = name

    # Abrir base de datos retornando cursor
    def __enter__(self):
        self.conn = sqlite3.connect(self.name)
        return self.conn.cursor()

    # Guardando y Cerrando base de datos
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()
        print('Comprobación de cambios y Conexión cerrada exitosamente')
