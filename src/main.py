from database.script.db_script import (
    sql_database, sql_productos, sql_credenciales)
from screen.login_screen import Sesion


def main():
    sql_database()  # <- Crear base de datos con columnas
    sql_credenciales()  # <- Crear ejemplos cliente y admin
    sql_productos()

    Sesion()  # <- Iniciar ventana root tkinter


if __name__ == '__main__':
    main()
