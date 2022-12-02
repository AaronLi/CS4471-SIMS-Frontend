import sqlite3

class CredentialDB:
    def __init__(self):
        self.conn = sqlite3.connect('auth.db')
        self.conn.commit()
        self.conn.execute("""CREATE TABLE IF NOT EXISTS credential (username TEXT PRIMARY KEY, hashedPw BLOB NOT NULL UNIQUE, token TEXT DEFAULT NULL, tokenTime FLOAT DEFAULT NULL)""")
        self.conn.execute("""INSERT INTO credential VALUES (?, ?, NULL, NULL)""",("hello",memoryview(b'$2a$12$sHfN9nB0TdUCz8IitUUpkuB.8TqD2BtPnk57Fd24XZUN48kSTle76')))
        self.cur = self.conn.cursor()

    def query(self, arg):
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def __del__(self):
        self.conn.close()
            

        