import sqlite3

class SQLite():
    #Constructor
    def __init__(self):
        self.db = sqlite3.connect('database/supermark_DB')
        self.cursor = sqlite3.cursor()

    #Abriendo conexion con la base de datos
    def enter(self):
        try:
            self.db
        except Exception as e:
            print('ERROR AL CONECTAR: ',e)

    #Guardar hacer Commit con la base de datos
    def save(self):
        print('Guardando cambios...')
        try:
            self.db.commit()
        except Exception as e:
            print('ERROR AL SUBiR DATOS: ',e)

    #Cerrando conexion con la base de datos
    def exit(self):
        print('Cerrando conexión...')
        try:
            self.db.close()
        except Exception as e:
            print('ERROR AL CERRAR: ',e)