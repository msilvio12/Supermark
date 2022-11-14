import shopping_cart
import card

class Cliente():
    def __init__(self, usuario, clave, nombre, apellido, direccion):
        self.usuario = usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.shopping_cart = shopping_cart.Carrito()
        self.card = card.Tarjeta()

    #Metodods definidos
    def actualizar_nombre(self, nombre):
        self.nombre = nombre

    def actualizar_apellido(self, apellido):
        self.apellido = apellido

    def actualizar_direccion(self, direccion):
        self.direccion = direccion

    def mostrar_datos():
        pass

    def __str__(self) -> str:
        pass