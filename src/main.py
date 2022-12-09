from sql.query import Consulta
from screen.login import Inicio


# Se instancia Consulta para crear la base de datos
def sql_database():

    base = Consulta()

    base.crear_tabla('administracion', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                        'usuario TEXT(20) NOT NULL UNIQUE',
                                        'clave TEXT(20) NOT NULL',
                                        'nombre TEXT(20) NOT NULL',
                                        'apellido TEXT(20) NOT NULL',
                                        'rol TEXT(20) NOT NULL'])

    base.crear_tabla('cliente', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                 'usuario TEXT(20) NOT NULL UNIQUE',
                                 'clave TEXT(20) NOT NULL',
                                 'nombre TEXT(20) NOT NULL',
                                 'apellido TEXT(20) NOT NULL',
                                 'direccion TEXT(50) NOT NULL'])

    base.crear_tabla('prodcuto', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                  'nombre TEXT NOT NULL',
                                  'marca TEXT NOT NULL',
                                  'categoria TEXT NOT NULL',
                                  'stock INTEGER NOT NULL',
                                  'precio REAL NOT NULL'])


# Se instancia Consulta para insertar valores a la base de datos
def sql_ejemplos():

    base = Consulta()

    base.insertar_cliente('cliente', ['usuario', 'clave', 'nombre', 'apellido', 'direccion'],
                          ['Magia', '1234', 'Homero', 'Simpson', 'Av. Siempreviva 742'])

    base.insertar_admin('administracion', ['usuario', 'clave', 'nombre', 'apellido', 'rol'],
                        ['Super', '1234', 'Magie', 'Simpson', 'Supervisor'])


def main():
    sql_database()
    sql_ejemplos()

    root = Inicio()
    root.mainloop()


if __name__ == '__main__':
    main()
