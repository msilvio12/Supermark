from sql.database import SQLite
from model.customer import Cliente
from model.product import Producto

#Funcion para crear o iniciar la base de datos si esta creada
def db():
    db = SQLite('src\database\Supermark.sqlite3')
    return db

def main():

    db()

    client1 = Cliente('magia','1234','pepe','gomez','avenida simpreviva 12')

    #Llamando al metodo getter
    print(client1.nombre)

    #Llamando al metodo setter
    client1.nombre = 'mario'

    #Llamando al metodo __repr__
    print(repr(client1))

if __name__ == '__main__':
    main()