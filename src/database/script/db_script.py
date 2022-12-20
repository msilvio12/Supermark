from sql.query import Consulta


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

    base.crear_tabla('productos', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                   'nombre TEXT NOT NULL UNIQUE',
                                   'categoria TEXT NOT NULL',
                                   'precio REAL NOT NULL',
                                   'stock INTEGER NOT NULL',
                                   'marca TEXT NOT NULL'])


# Se instancia Consulta para insertar valores a la base de datos
def sql_credenciales():

    base = Consulta()

    base.insertar_cliente('cliente',
                          ['usuario',
                           'clave',
                           'nombre',
                           'apellido',
                           'direccion'],
                          ['Rosquilla',
                           '1234',
                           'Homero',
                           'Simpson',
                           'Av. Siempreviva 742'])

    base.insertar_admin('administracion',
                        ['usuario',
                         'clave',
                         'nombre',
                         'apellido',
                         'rol'],
                        ['Magia',
                         '1234',
                         'Magie',
                         'Simpson',
                         'Supervisor'])


def sql_productos():

    base = Consulta()

    lista = [('coca-cola', 'bebidas',  660, 500, 'Envase 3lts'),
             ('vino', 'bebidas',  600, 1000, 'Envase 1lts'),
             ('soda mineral', 'bebidas',  100, 100, 'Envase 1.5lts'),
             ('fernet', 'bebidas',  500, 700, 'Envase 1lts'),
             ('cerveza', 'bebidas',  400, 2200, 'Envase 1lts'),
             ('energizante', 'bebidas',  280, 800, 'Envase 350cm3'),
             ('fanta', 'bebidas',  500, 300, 'Envase 2.5lts'),
             ('ice', 'bebidas',  250, 200, 'Envase 3lts'),
             ('licor', 'bebidas', 456, 500, 'Envase de 1lt'),
             ('hamburguesa', 'refrigerados', 680, 1500, 'pack de 6 unidades'),
             ('huevo', 'refrigerados', 200, 3000, 'pack de 6 unidades'),
             ('fiambre', 'refrigerados', 100, 300, 'pack queso'),
             ('helado', 'refrigerados', 150, 621, 'Envase de 1kg'),
             ('salchicha', 'refrigerados', 250, 500, 'Envase 250 gr'),
             ('leche', 'refrigerados', 489, 1000, 'Envase 1lts'),
             ('manteca', 'refrigerados', 285, 1400, 'Envase de 150 gr'),
             ('yogur', 'refrigerados', 621, 1800, 'Envase de 1lts'),
             ('azucar', 'almacen',  200, 400, 'Envase 1kg'),
             ('arroz', 'almacen',  170, 200, 'Envase 1kg'),
             ('caldo', 'almacen',  50, 300, 'Caja de 10 unidades'),
             ('aceite', 'almacen',  600, 700, 'Envase 900cm3'),
             ('vinagre', 'almacen',  150, 200, 'Envase 350cm3'),
             ('sal', 'almacen',  50, 200, 'Envase 250grs'),
             ('harina', 'almacen',  250, 100, 'Envase 1kg'),
             ('dulce de leche', 'almacen',  350, 600, 'Envase 250cm3'),
             ('galletitas', 'almacen',  200, 1000, 'pack de 3 unidades'),
             ('cafe', 'almacen',  390, 300, 'Envase 1kg'),
             ('te', 'almacen',  400, 350, 'Caja de 100 unidades'),
             ('mate cocido', 'almacen', 240, 1000, 'Caja de 100 unidades'),
             ('yerba', 'almacen',  750, 1200, 'Envase 1kg'),
             ('polenta', 'almacen', 195, 1500, 'Envase de 1kg'),
             ('mermelada', 'almacen',  450, 800, 'Envase 350gr'),
             ('papel higienico', 'limpieza',  670, 2200, 'pack de 4 Unidades'),
             ('servilleta', 'limpieza',  290, 600, 'pack de 2 unidades'),
             ('jabon liquido', 'limpieza',  950, 500, 'Envase 3lts'),
             ('jabon tocador', 'limpieza',  100, 600, 'Envase 150gr'),
             ('lavavajilla', 'perfumeria',  150, 700, 'Envase 900cm3'),
             ('cremas corporales', 'perfumeria',  410, 500, 'Envase 85gr'),
             ('desodorante corporal', 'perfumeria',  230, 500, 'Envase 100cm3')
             ]

    for item in lista:
        # for item in lista:
        base.insertar_producto('productos', ['nombre',
                                             'categoria',
                                             'precio',
                                             'stock',
                                             'marca'], item)
