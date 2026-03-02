from admin import Admin
from reservation import Reservation
from groups import Groupe
from creneau import Creneau
from exporte import Exporter


class Application:

    def __init__(self):
        self.__admin = Admin()
        self.__reservation = Reservation()
        self.__groupe = Groupe()
        self.__creneau = Creneau()
        self.__exporter = Exporter()


 
    def inscrire_admin(self):
        print("\n********INSCRIPTION ADMIN *******")
        username = input("Nouveau login : ")
        password = input("Nouveau mot de passe : ")

        self.__admin.inscrire(username, password)

    def authentification(self):
        print("\n===== AUTHENTIFICATION =====")
        username = input("Login : ")
        password = input("Mot de passe : ")

        if not self.__admin.login(username, password):
            print("Accès refusé")
            return False

        print("Connexion réussie")
        return True


 
    def afficher_menu(self):
        print("\n===== MENU =====")
        print("0. Inscrire un administrateur")
        print("1. Vue Globale")
        print("2. Vue Disponibilités")
        print("3. Ajouter Groupe")
        print("4. Ajouter Créneau")
        print("5. Réserver un Créneau")
        print("6. Export CSV")
        print("7. Quitter")


 
    def lancer(self):
           
            if not self.authentification():
                return False

            while True:
                self.afficher_menu()
                choix = input("Choix : ")

                match choix:

                    case "0":
                        self.inscrire_admin()


                    case "1":
                    
                        date = input("Date (YYYY-MM-DD) : ")
                        resultat = self.__reservation.planning_journalier(date)

                        print("\n===== PLANNING GLOBAL =====")
                        for r in resultat:
                            groupe_nom = r["nom"] if r["nom"] else "[LIBRE]"
                            print(f"{r['heure_debut']} - {r['heure_fin']} | {groupe_nom}")


                    case "2":
                        
                        date = input("Date (YYYY-MM-DD) : ")
                        resultat = self.__reservation.disponibilites(date)

                        print("\n===== CRENEAUX DISPONIBLES =====")
                        for r in resultat:
                            print(f"{r['heure_debut']} - {r['heure_fin']}")


                    case "3":
                        

                        nom = input("Nom du groupe : ")
                        responsable = input("Responsable : ")
                        self.__groupe.ajouter(nom, responsable)
                        print("Groupe ajouté avec succès")


                    case "4":
                    

                        debut = input("Heure début (HH:MM:SS) : ")
                        fin = input("Heure fin (HH:MM:SS) : ")
                        self.__creneau.ajouter(debut, fin)
                        print("Créneau ajouté avec succès")


                    case "5":
                    
                        date = input("Date : ")
                        motif = input("Motif : ")
                        groupe_id = int(input("ID Groupe : "))
                        creneau_id = int(input("ID Créneau : "))
                        self.__reservation.reserver(date, motif, groupe_id, creneau_id)


                    case "6":
                    

                        date = input("Date : ")
                        self.__exporter.exporter(date)


                    case "7":
                        print("Fin du programme")
                        break


                    case _:
                        print("Choix invalide")



if __name__ == "__main__":
    app = Application()
    app.lancer()