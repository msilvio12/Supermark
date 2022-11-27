#from tkinter import Tk
#from screen.home import Inicio


from sql.query import Consulta


def main():
    #root = Inicio(Tk())
    # root.mainloop()
    base = Consulta()
    base.crear_tabla('cliente', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                 'usuario TEXT(15) NOT NULL UNIQUE',
                                 'clave TEXT(15) NOT NULL',
                                 'nombre TEXT(20) NOT NULL',
                                 'apellido TEXT(20) NOT NULL',
                                 'direccion TEXT(50) NOT NULL'])

    base.insertar_registro('cliente', ['usuario', 'clave', 'nombre', 'apellido', 'direccion'],
                           ["'magia'", '123', "'Mario'", "'Pepe'", "'Av. Libertad'"])


if __name__ == '__main__':
    main()
