from customer import Cliente

def main():

    client1 = Cliente('magia','1234','pepe','gomez','avenida simpreviva 12')

    #Llamando al metodo getter
    print(client1.nombre)

    #Llamando al metodo setter
    client1.nombre = 'mario'

    #Llamando al metodo __repr__
    print(repr(client1))

if __name__ == '__main__':
    main()