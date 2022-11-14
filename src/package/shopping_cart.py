import product

class Carrito():

    def __init__(self, producto: product.Producto):
            self.limite = 30
            self.mi_carrito = [producto]

    #Metodo para agregar objetos Producto al carrito usando diccionario
    def agregar(self, item, cantidad):
        if item not in self.mi_carrito:
            self.mi_carrito.append(item)
        return self.mi_carrito

    def subtotal(self):
        pass