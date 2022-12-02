import sqlite3

class CredentialDB:
    def __init__(self):
        self.conn = sqlite3.connect('auth.db')
        self.conn.commit()
        self.conn.execute("CREATE TABLE IF NOT EXISTS (username TEXT PRIMARY KEY, hashedPw BLOB NOT NULL UNIQUE, token TEXT, tokenTime FLOAT")
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()
            

        