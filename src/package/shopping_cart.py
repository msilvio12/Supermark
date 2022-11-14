import product

class Carrito():

    def __init__(self):
            self.limite = 30
            self.mi_carrito = []

    #Metodo para agregar objetos Producto al carrito usando diccionario
    def agregar(self, item: product.Producto, cantidad):
        if item not in self.mi_carrito:
            self.mi_carrito.append(item)
        return self.mi_carrito

    def subtotal(self):
        pass