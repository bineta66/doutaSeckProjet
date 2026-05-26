import mysql.connector

class Database:

    IntegrityError = mysql.connector.IntegrityError

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hellome13",
            database="centre_douta_seck"
        )

        self.cursor = self.conn.cursor(dictionary=True)

    def execute(self, query, params=None, commit=False):
        # mysql-connector accepte execute(query) quand params est None.
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)

        if commit:
            self.conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()