import database

class Table():

    #Metdodo para crear la tablas en la base de datos
    def user_table(self, table_name, columns):
        sql = database.Connection.enter()
        sql.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        
        database.Connection().save()
        database.Connection().exit()
