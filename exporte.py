from db import Database
import csv

class Exporter:

    def exporter_csv(self,date_reservation):
        donne=Database()
        sql="""SELECT c.heure_debut, c.heure_fin,
               g.nom, r.motif, g.responsable
            FROM reservations r
            JOIN creneaux c ON r.id_creneaux = c.id_creneaux
            JOIN groupes g ON r.id_groupe = g.id_groupe
            WHERE r.date_reservation = %s
            ORDER BY c.heure_debut
            """
        donne.execute(sql,(date_reservation,))
        resultat=donne.fetchall()
        donne.close()

        with open("Jounalier.csv","w") as f:
            writer = csv.writer(f)
            writer.writerow(["Heure début", "Heure fin", "Groupe", "Motif", "Responsable"])

            for row in resultat:
                writer.writerow([
                    row["heure_debut"],
                    row["heure_fin"],
                    row["nom"],
                    row["motif"],
                    row["responsable"]
                ])

        print("journalier.csv généré.")