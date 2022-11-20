from model.payment import Tarjeta
from model.cart import Carrito
from model.product import Producto


class Cliente:

    def __init__(self, usuario : str, clave : str, nombre: str, apellido: str, direccion: str):
        self._usuario = usuario
        self._clave = clave
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._tarjeta = Tarjeta(0.0)
        self._carrito = Carrito(30, 0)

    #Metodos getter y setter
    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario : str):
        self._usuario = usuario

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave : str):
        self._clave = clave

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre : str):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido : str):
        self._apellido = apellido

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion : str):
        self._direccion = direccion

    #Metodo magico informal para mostrar el objeto al momento de llamarlo con print
    def __str__(self) -> str:
        return f"Nombre: {self._nombre} Apellido: {self._apellido}"

    #Metodo magico formal para mostrar el objeto al momento de llamarlo con print
    def __repr__(self) -> str:
        return f'Cliente("{self._usuario}","{self._clave}","{self._nombre}","{self._apellido}""{self._direccion}",)'

    #Metodo catalogo de productos
    def catalogo(self):
        pass