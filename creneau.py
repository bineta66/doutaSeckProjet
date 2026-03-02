from db import Database

class Creneau:

    def ajouter(self, debut, fin):
        db = Database()
        db.execute("INSERT INTO creneaux(heure_debut, heure_fin) VALUES(%s,%s)", (debut, fin), commit=True)
        db.close()

    def lister(self):
        db = Database()
        db.execute("SELECT * FROM creneaux ORDER BY heure_debut")
        resultat = db.fetchall()
        db.close()
        return resultat