from db import Database

class Reservation:

    def reserver(self, date, motif, id_groupe, id_creneaux):
        db = Database()
        db.execute("SELECT id FROM reservations WHERE date_reservation=%s AND id_creneaux=%s", (date, id_creneaux))
        if db.fetchone():
            db.close()
            print("Créneau déjà occupé !")
            return False
        db.execute("INSERT INTO reservations(date_reservation, motif, id_groupe, id_creneaux) VALUES(%s,%s,%s,%s)",
                   (date, motif, id_groupe, id_creneaux), commit=True)
        db.close()
        print("Réservation validée")
        return True

    def planning_journalier(self, date):
        db = Database()
        query = """SELECT c.heure_debut, c.heure_fin, g.nom, r.motif
                   FROM creneaux c
                   LEFT JOIN reservations r ON c.id_creneaux = r.id_creneaux AND r.date_reservation=%s
                   LEFT JOIN groupes g ON r.id_groupe = g.id_groupe
                   ORDER BY c.heure_debut"""
        db.execute(query, (date,))
        resultat = db.fetchall()
        db.close()
        return resultat

    def disponibilites(self, date):
        db = Database()
        query = """SELECT * FROM creneaux WHERE id_creneaux NOT IN (
                        SELECT id_creneaux FROM reservations WHERE date_reservation=%s
                   ) ORDER BY heure_debut"""
        db.execute(query, (date,))
        resultat = db.fetchall()
        db.close()
        return resultat
    
    
    def annuler_reservation(self, date, id_creneaux):
        db = Database()

        try:
        
            db.execute("""
                SELECT id FROM reservations
                WHERE date_reservation = %s AND id_creneaux = %s
            """, (date, id_creneaux))

            reservation = db.fetchone()

            if not reservation:
                print("Aucune réservation trouvée pour cette date et ce créneau.")
                db.close()
                return False

           
            db.execute("""
                DELETE FROM reservations
                WHERE date_reservation = %s AND id_creneaux = %s
            """, (date, id_creneaux), commit=True)

            print("Réservation annulée avec succès.")
            db.close()
            return True

        except Exception as e:
            print("Erreur lors de l'annulation :", e)
            db.close()
            return False