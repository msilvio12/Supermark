class Table():

    def __init__(self, db):
        self.db = db

    #Metdodo para crear la tablas en la base de datos
    def user_table(self, table_name):
        sql = self.db.enter()
        print(type(sql))
        #sql.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        
        #database.Connection().save()
        #database.Connection().exit()
