from logic.product import Producto

class Carrito():

    def __init__(self,limite : int, cantidad : int):
        self.limite = limite
        self.cantidad = cantidad
        self.lista = []

    #Metodo para agregar objetos Producto al carrito usando diccionario
    def agregar(self, item: Producto, cantidad):
        if item not in self.lista:
            self.lista.append(item)
        return self.lista

    def subtotal(self):
        pass