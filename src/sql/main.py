import database
import table

if __name__ == '__main__':
    db = database.SQLite('src\database\Supermark.sqlite3')
    table = table.Table(db)
    table.user_table('usuarios')