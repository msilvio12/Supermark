class Producto():

    def __init__(self,nombre, marca, categoria,stock, precio):
        self.nombre = nombre
        self.marca = marca
        self.categoria = categoria
        self.stock = stock
        self.precio = precio

    #Metodo para actualizar nombre
    def actualizar_nombre(self, nombre):
        self.nombre = nombre

    #Metodo para actualizar marca
    def atualizar_marca(self, marca):
        self.marca = marca

    #Metodo para actualizar categoria
    def atualizar_categoria(self, categoria):
        self.categoria = categoria

    #Metodo para actualizar stock
    def actualizar_stock(self, stock):
        self.stock = stock

    #Metodo para actualizar precio
    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self) -> str:
        return f"Name: {self.nombre}\nPrice: {self.precio}"