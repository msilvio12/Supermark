from sql.database import SQLite


class Consulta:
    def __init__(self):
        self._db = SQLite('src/database/Supermark.sqlite3')

    def crear_tabla(self, tabla_nombre: str, columna_nombre: list[str]):
        try:
            with self._db as cur:
                cur.execute(
                    f"CREATE TABLE IF NOT EXISTS {tabla_nombre}('{columna_nombre}');")
        except Exception as e:
            print(e)

    # Insertar un registro
    def insertar_registro(self, tabla_nombre: str, columna_nombre: str, nuevo_valor):
        try:
            with self._db as cur:
                cur.execute(
                    f"""INSERT INTO {tabla_nombre} ({columna_nombre})
                        VALUES('{nuevo_valor}');""")
        except Exception as e:
            print(e)

    # Agrega una columna a una tabla
    def agregar_columna(self, tabla_nombre: str, nuevo_valor: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""ALTER TABLE {tabla_nombre}
                        ADD COLUMN {nuevo_valor};""")
        except Exception as e:
            print(e)

    # Renombrar una tabla
    def renombrar_tabla(self, tabla_nombre: str, nuevo_valor: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""ALTER TABLE {tabla_nombre}
                        RENAME TO {nuevo_valor};""")
        except Exception as e:
            print(e)

    # Renombrar una columna de una tabla
    def renombrar_columna(self, tabla_nombre: str, columna_nombre: str, nuevo_valor: str):
        try:
            with self._db as cur:
                cur.execute(
                    f"""ALTER TABLE {tabla_nombre}
                        RENAME COLUMN {columna_nombre} TO {nuevo_valor};""")
        except Exception as e:
            print(e)

    # Actualizar un registro de una columna a la vez
    def actualizar_registro(self, tabla_nombre: str, columna_nombre: str, nuevo_valor, columna_id: str, id: int):
        try:
            with self._db as cur:
                cur.execute(
                    f"""UPDATE {tabla_nombre}
                        SET {columna_nombre} = {nuevo_valor}
                        WHERE {columna_id} = {id};""")
        except Exception as e:
            print(e)
