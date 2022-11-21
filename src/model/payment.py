from model.customer import Cliente


class Tarjeta(Cliente):

    def __init__(self, usuario: str, clave: str, nombre: str, apellido: str, direccion: str, saldo: float):
        super().__init__(usuario, clave, nombre, apellido, direccion)
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float):
        if saldo > 0:
            self._saldo = saldo
        else:
            print('No es posible cargar saldo negativo')
