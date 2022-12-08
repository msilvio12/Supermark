from sql.query import Consulta
from screen.login import Inicio


def sql_ejemplos():
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

    base.insertar_registro('cliente', ['usuario', 'clave', 'nombre', 'apellido', 'direccion'],
                           ["'Magia'", '1234', "'Mario'", "'Pepe'", "'Av. Libertad'"])


def main():
    sql_ejemplos()

    root = Inicio()
    root.mainloop()


if __name__ == '__main__':
    main()
