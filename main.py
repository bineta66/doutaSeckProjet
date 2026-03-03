# main.py
from admin import Admin
from reservation import Reservation
from groups import Groupe
from creneau import Creneau
from exporte import Exporter
from saisie import *
from getpass import getpass





class Application:

    def __init__(self):
        self.__admin = Admin()
        self.__reservation = Reservation()
        self.__groupe = Groupe()
        self.__creneau = Creneau()
        self.__exporter = Exporter()
        self.__connecte = False  

    def inscrire_admin(self):
        print("\n******** INSCRIPTION ADMIN *******")
        username = demander_saisie_non_vide("Nouveau login : ")
        password = getpass("Nouveau mot de passe : ")
        self.__admin.inscrire(username, password)

   
    def authentification(self):
        print("\n********* AUTHENTIFICATION *********")
        username = demander_saisie_non_vide("Login : ")
        password = getpass("Mot de passe : ")
        if not self.__admin.login(username, password):
            print("Accès refusé")
            return False
        print("Connexion réussie")
        return True

    def afficher_menu(self):
        print("\n==============================")
        print("        MENU PRINCIPAL        ")
        print("==============================")
        print("1. Vue globale (planning journalier)")
        print("2. Voir créneaux disponibles")
        print("3. Ajouter un groupe")
        print("4. Ajouter un créneau")
        print("5. Lister les groupes")
        print("6. Lister les créneaux")
        print("7. Réserver un créneau")
        print("8. Annuler une réservation")
        print("9. Exporter le planning en CSV")
        print("0. Quitter")

  
    def lancer(self):
    
        while not self.__connecte:
            self.__connecte = self.authentification()
        while True:
                self.afficher_menu()
                choix = input("Choix : ").strip()

                match choix:

                    case "1":
                        date = demander_date_non_vide()
                        resultat = self.__reservation.planning_journalier(date)
                        print("\n===== PLANNING GLOBAL =====")
                        for r in resultat:
                            groupe_nom = r["nom"] if r["nom"] else "[LIBRE]"
                            print(f"{r['heure_debut']} - {r['heure_fin']} | {groupe_nom} | {r.get('motif','')}")

                    case "2":
                        date = demander_date_non_vide()
                        resultat = self.__reservation.disponibilites(date)
                        print("\n===== CRENEAUX DISPONIBLES =====")
                        for r in resultat:
                            print(f"{r['heure_debut']} - {r['heure_fin']}")

                    case "3":
                        nom = demander_alpha("Nom du groupe : ")
                        responsable = demander_alpha("Responsable : ")
                        self.__groupe.ajouter(nom, responsable)
                        print("Groupe ajouté avec succès")

                    case "4":
                        debut = demander_heure_non_vide("Heure début (HH:MM:SS) : ")
                        fin = demander_heure_non_vide("Heure fin (HH:MM:SS) : ")
                        self.__creneau.ajouter(debut, fin)
                        print("Créneau ajouté avec succès")

                    case "5":
                        groupes = self.__groupe.lister_groupes()
                        print("\n===== LISTE DES GROUPES =====")
                        for g in groupes:
                            print(f"ID: {g['id']} | Nom: {g['nom']} | Responsable: {g['responsable']}")

                    case "6":
                        creneaux = self.__creneau.lister_creneaux()
                        print("\n===== LISTE DES CRENEAUX =====")
                        for c in creneaux:
                            print(f"ID: {c['id']} | {c['heure_debut']} - {c['heure_fin']}")

                    case "7":
                        print("\n--- Groupes disponibles ---")
                        for g in self.__groupe.lister_groupes():
                            print(f"ID: {g['id']} | {g['nom']}")

                        print("\n--- Créneaux disponibles ---")
                        for c in self.__creneau.lister_creneaux():
                            print(f"ID: {c['id']} | {c['heure_debut']} - {c['heure_fin']}")

                        date = demander_date_non_vide()
                        motif = demander_saisie_non_vide("Motif : ")
                        groupe_id = demander_entier("ID Groupe : ")
                        creneau_id = demander_entier("ID Créneau : ")

                        self.__reservation.reserver(date, motif, groupe_id, creneau_id)

                    case "8":
                        date = demander_date_non_vide()
                        creneau_id = demander_entier("ID Créneau à annuler : ")
                        self.__reservation.annuler_reservation(date, creneau_id)

                    case "9":
                        date = demander_date_non_vide()
                        self.__exporter.exporter(date)

                    case "0":
                        print("Fin du programme")
                        break

                    case _:
                        print("Choix invalide")


if __name__ == "__main__":
    app = Application()
    app.lancer()