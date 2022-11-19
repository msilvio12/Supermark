class Producto():

    def __init__(self,nombre : str, marca : str, categoria : str,stock : int, precio : float):
        self._nombre = nombre
        self._marca = marca
        self._categoria = categoria
        self._stock = stock
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre : str):
        self._nombre = nombre

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca : str):
        self._marca = marca

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria : str):
        self._categoria = categoria

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock : int):
        self._stock = stock

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio : float):
        self._precio = precio
    
    def __str__(self) -> str:
        return f"Name: {self.nombre}\nPrice: {self.precio}"