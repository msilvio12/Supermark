from screen.login_screen import Sesion
from database.script import db_script


def main():
    db_script.sql_database()  # <- Crear base de datos con columnas
    db_script.sql_credenciales()  # <- Crear ejemplos cliente y admin

    Sesion()  # <- Iniciar ventana root tkinter


if __name__ == '__main__':
    main()
