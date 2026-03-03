# export_csv.py
import csv
from db import Database
import csv

class Exporter:

    def exporter(self, date_reservation):

        db = Database()

       
        query = """
        SELECT c.heure_debut, c.heure_fin, g.nom AS groupe, r.motif, g.responsable
        FROM creneaux c
        LEFT JOIN reservations r
               ON c.id_creneaux = r.id_creneaux AND r.date_reservation = %s
        LEFT JOIN groupes g
               ON r.id_groupe = g.id_groupe
        ORDER BY c.heure_debut
        """
        try:
            db.execute(query, (date_reservation,))
            resultat = db.fetchall()
        except Exception as e:
            print("Erreur lors de la récupération des données :", e)
            db.close()
            return

        db.close()

        if not resultat:
            print("Aucune réservation pour cette date.")
            return

        fiche = f"planning_{date_reservation}.csv"

    
        try:
            with open(fiche, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Heure début", "Heure fin", "Groupe", "Motif", "Responsable"])
                for r in resultat:
                    writer.writerow([
                        r["heure_debut"],
                        r["heure_fin"],
                        r["groupe"] if r["groupe"] else "[LIBRE]",
                        r["motif"] if r["motif"] else "",
                        r["responsable"] if r["responsable"] else ""
                    ])
            print(f"Export CSV réalisé avec succès : {fiche}")
        except Exception as e:
                print("Erreur lors de l'écriture du fichier CSV :", e)