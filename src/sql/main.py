import database
import table

if __name__ == '__main__':
    db = database.Connection('src\database\Supermark.sqlite3')
    table = table.Table.user_table('usuarios','')