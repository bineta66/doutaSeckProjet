from datetime import datetime

def demander_saisie_non_vide(prompt):
    while True:
        valeur = input(prompt).strip()
        if valeur:
            return valeur
        print("La saisie ne peut pas être vide !")

def demander_alpha(prompt):
    while True:
        valeur = input(prompt).strip()
        if valeur.replace(" ", "").isalpha():  
            return valeur
        print("La saisie doit contenir uniquement des lettres !")

def demander_entier(prompt):
    while True:
        valeur = input(prompt).strip()
        if valeur.isdigit():
            return int(valeur)
        print("Veuillez saisir un nombre entier valide !")

def demander_date_non_vide(prompt="Date (YYYY-MM-DD) : "):
    while True:
        date_str = input(prompt).strip()
        if not date_str:
            print("La saisie ne peut pas être vide !")
            continue
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Date invalide ! Utilisez le format YYYY-MM-DD.")

def demander_heure_non_vide(prompt="Heure (HH:MM:SS) : "):
    while True:
        heure_str = input(prompt).strip()
        if not heure_str:
            print("La saisie ne peut pas être vide !")
            continue
        try:
            datetime.strptime(heure_str, "%H:%M:%S")
            return heure_str
        except ValueError:
            print("Heure invalide ! Utilisez le format HH:MM:SS.")