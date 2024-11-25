import sqlite3


class Connection:
    
    def __init__(self):
        self.cursor = self.db_connection().cursor()

    def db_connection(self):
        try:
            conn = sqlite3.connect("database.db")
            return conn
        except sqlite3.OperationalError as e:
            print(" Failed to open database: ", e)
    
    def login(self, email, password):
        self.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        result = self.cursor.fetchone()

    def create_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT NOT NULL, phone TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)''')
        print('Successfully created new table')