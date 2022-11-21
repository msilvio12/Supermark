from sql.query import Consulta


def main():

    db = Consulta()
    db.crear_tabla('cliente', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                               'usuario TEXT NOT NULL UNIQUE',
                               'clave TEXT NOT NULL',
                               'nombre TEXT NOT NULL',
                               'apellido TEXT NOT NULL',
                               'direccion TEXT NOT NULL'])


if __name__ == '__main__':
    main()
