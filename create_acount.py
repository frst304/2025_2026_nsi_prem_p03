import sys
import os

# On importe la liste 'users' depuis le fichier 'data_users.py'
from data_users import users

# Définition de la fonction pour créer un compte utilisateur
def create_acount_fctn():
    # Efface l'écran (fonctionne sous Windows)
    os.system('cls')

    # Demande à l'utilisateur de saisir son nom complet
    # On enlève les espaces superflus et on met tout en minuscules
    name = input("Entrez votre nom complet : ").strip().lower()

    # Demande à l'utilisateur de saisir son âge (converti en entier)
    age = int(input("Entrez votre âge : "))

    # Crée automatiquement un identifiant à partir du prénom et du nom
    # Exemple : "Jean Dupont" devient "j.dupont"
    username = name.split()[0][0] + "." + name.split()[-1]

    # Demande à l'utilisateur de choisir un mot de passe
    password = input("Choisissez un mot de passe : ").strip()

    # Crée un dictionnaire représentant le nouvel utilisateur
    user = {
        'id': username,            # Identifiant généré automatiquement
        'password': password,      # Mot de passe choisi
        'name': name,              # Nom complet de l'utilisateur
        'age': age,                # Âge de l'utilisateur
        'balance_account': 0.0     # Solde du compte initialisé à 0
    }

    # Ajoute ce nouvel utilisateur à la liste 'users'
    users.append(user)

    # Affiche un message de confirmation avec l'identifiant généré
    print(f"Compte créé avec succès. Votre identifiant est : {username}")

    # Attend que l'utilisateur appuie sur Entrée avant de continuer
    input("Appuyez sur Entrée pour continuer...")

    # Retourne les informations du nouvel utilisateur
    return user