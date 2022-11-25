from sql.query import Consulta


db = Consulta()
db.crear_tabla('administracion', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                                  'usuario TEXT NOT NULL UNIQUE',
                                  'clave TEXT NOT NULL',
                                  'nombre TEXT NOT NULL',
                                  'apellido TEXT NOT NULL',
                                  'rol TEXT NOT NULL'])

db.crear_tabla('cliente', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                           'usuario TEXT NOT NULL UNIQUE',
                           'clave TEXT NOT NULL',
                           'nombre TEXT NOT NULL',
                           'apellido TEXT NOT NULL',
                           'direccion TEXT NOT NULL'])

db.crear_tabla('prodcuto', ['id INTEGER PRIMARY KEY AUTOINCREMENT',
                            'nombre TEXT NOT NULL',
                            'marca TEXT NOT NULL',
                            'categoria TEXT NOT NULL',
                            'stock INTEGER NOT NULL',
                            'precio REAL NOT NULL'])
