import mysql.connector

class Database:

    def __init__(self):
        self.__connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hellome13",
            database="centre_douta_seck"
        )
        self.__cursor = self.__connexion.cursor(dictionary=True)

  
    def execute(self, query, params=None, commit=False):
        self.__cursor.execute(query, params or ())
        if commit:
            self.__connexion.commit()

    def fetchall(self):
        return self.__cursor.fetchall()

    def fetchone(self):
        return self.__cursor.fetchone()

    def close(self):
        self.__cursor.close()
        self.__connexion.close()