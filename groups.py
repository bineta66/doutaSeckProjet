from db import Database

class Groupe:

    def ajouter(self, nom, responsable):
        db = Database()
        db.execute("INSERT INTO groupes(nom,responsable) VALUES(%s,%s)", (nom,responsable), commit=True)
        db.close()

    def lister(self):
        db = Database()
        db.execute("SELECT * FROM groupes")
        resultat = db.fetchall()
        db.close()
        return resultat