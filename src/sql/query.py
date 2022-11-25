from sql.database import SQLite


class Consulta:
    def __init__(self):
        self._db = SQLite("src/database/Supermark.sqlite3")

    # Crear tabla formateando la lista recibida para pasarla como consulta
    def crear_tabla(self, tabla_nombre: str, lista_columna: list[str]):
        try:
            with self._db as cur:
                columna_nombre = ", ".join(lista_columna)
                cur.execute(
                    f"CREATE TABLE IF NOT EXISTS {tabla_nombre}({columna_nombre});"
                )
        except Exception as e:
            print(e)

    # Insertar un registro
    def insertar_registro(self, tabla_nombre: str, columna_nombre: str, nuevo_valor):
        try:
            with self._db as cur:
                cur.execute(
                    f"""INSERT INTO {tabla_nombre} ({columna_nombre})
                        VALUES('{nuevo_valor}');"""
                )
        except Exception as e:
            print(e)

    # Buscar en una tabla y traer una columna
    def buscar_registro(self, tabla_nombre: str, columna_nombre: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""SELEC {columna_nombre} FROM {tabla_nombre}"""
                )
        except Exception as e:
            print(e)

    # Buscar en una tabla y traer todas las columnas
    def buscar_todo(self, tabla_nombre: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""SELEC * FROM {tabla_nombre}"""
                )
        except Exception as e:
            print(e)

    # Agrega una columna a una tabla
    def agregar_columna(self, tabla_nombre: str, nuevo_valor: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""ALTER TABLE {tabla_nombre}
                        ADD COLUMN {nuevo_valor};"""
                )
        except Exception as e:
            print(e)

    # Renombrar una tabla
    def renombrar_tabla(self, tabla_nombre: str, nuevo_valor: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""ALTER TABLE {tabla_nombre}
                        RENAME TO {nuevo_valor};"""
                )
        except Exception as e:
            print(e)

    # Renombrar una columna de una tabla
    def renombrar_columna(
            self, tabla_nombre: str, columna_nombre: str, nuevo_valor: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""ALTER TABLE {tabla_nombre}
                        RENAME COLUMN {columna_nombre} TO {nuevo_valor};"""
                )
        except Exception as e:
            print(e)

    # Actualizar un registro de una columna a la vez
    def actualizar_registro(self, tabla_nombre: str, columna_nombre: str, nuevo_valor, columna_id: str, id: int,):
        try:
            with self._db as cur:
                cur.execute(
                    f"""UPDATE {tabla_nombre}
                        SET {columna_nombre} = {nuevo_valor}
                        WHERE {columna_id} = {id};"""
                )
        except Exception as e:
            print(e)