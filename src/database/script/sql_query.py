from sql.query import Consulta


db = Consulta()
db.crear_tabla('administracion', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                  'usuario TEXT(20) NOT NULL UNIQUE',
                                  'clave TEXT(20) NOT NULL',
                                  'nombre TEXT(20) NOT NULL',
                                  'apellido TEXT(20) NOT NULL',
                                  'rol TEXT(20) NOT NULL'])

db.crear_tabla('cliente', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                           'usuario TEXT(20) NOT NULL UNIQUE',
                           'clave TEXT(20) NOT NULL',
                           'nombre TEXT(20) NOT NULL',
                           'apellido TEXT(20) NOT NULL',
                           'direccion TEXT(50) NOT NULL'])

db.crear_tabla('prodcuto', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                            'nombre TEXT NOT NULL',
                            'marca TEXT NOT NULL',
                            'categoria TEXT NOT NULL',
                            'stock INTEGER NOT NULL',
                            'precio REAL NOT NULL'])
