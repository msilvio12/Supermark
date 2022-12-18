from model.product import Producto


class Carrito:
    def __init__(self, limite: int, cantidad: int):
        self._limite = limite  # <--- Limite del carrito 30
        self._cantidad = cantidad  # <--- cantidad del carrito comienza en 0
        self.lista = []

    # Metodos getter y setter
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    # Metodo para comprobar si un producto tiene stock suficiente para operar la demanda del cliente
    def comprobar_cantidad(self, item: Producto, cantidad: int):
        return item.stock > cantidad

    # Metodo para comprobar si el objeto ya se encuentar en el carrito
    def comprobar_duplicado(self, item: Producto):
        return item in self.lista

    # Metodo para agregar objetos Producto al carrito llamando a otros metodos para comprobar
    def agregar(self, item: Producto, cantidad: int):
        if self.comprobar_cantidad(item, cantidad):
            if self.comprobar_duplicado(item):
                self.lista.append(item)
            else:
                print("El objeto ya se encuentra en el carrito")
        else:
            print("No hay suficiente stock")

        return self.lista

    def subtotal(self):
        pass
