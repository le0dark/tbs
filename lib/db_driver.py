import sqlite3


class Connection:
    
    def __init__(self):
        self.conn = self.db_connection()

    def db_connection(self):
        try:
            conn = sqlite3.connect("database.db")
            return conn
        except sqlite3.OperationalError as e:
            print(" Failed to open database: ", e)
    
    def login(self, email, password):
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password)).close()
        result = cursor.fetchone()

    def create_database(self):
        conn = self.conn
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT NOT NULL, phone TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)''')
        print('Successfully created new table')