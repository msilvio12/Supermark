import sqlite3

class Connection:
    #Constructor
    def __init__(self,name):
        self.name = name
        self.con = sqlite3.connect(self.name)
        self.cursor = self.con.cursor()

    #Abriendo conexion con la base de datos
    def enter(self):
        try:
            self.con
        except Exception as e:
            print('ERROR AL CONECTAR: ',e)
        return self.cursor

    #Guardar hacer Commit con la base de datos
    def save(self):
        print('Guardando cambios...')
        try:
            self.con.commit()
        except Exception as e:
            print('ERROR AL SUBiR DATOS: ',e)

    #Cerrando conexion con la base de datos
    def exit(self):
        print('Cerrando conexión...')
        try:
            self.con.close()
        except Exception as e:
            print('ERROR AL CERRAR: ',e)