import sys
import os

# On ajoute le dossier 'user_actions' au chemin d'accès système
# pour pouvoir importer des modules qui s’y trouvent
sys.path.append(os.path.join(os.getcwd(), 'user_actions'))

# On importe la fonction de connexion depuis le fichier login.py
from login import login_fctn
from add_money import add_money_fctn
from pull_money import pull_money_fctn
from view_sold import view_sold_fctn

from create_acount import create_acount_fctn


def menu_fctn():
    # On appelle la fonction de connexion et on récupère les infos de l’utilisateur
    user = login_fctn()
    # On efface l’écran (fonctionne sur Windows)
    os.system('cls')
    # On affiche le menu principal pour l’utilisateur connecté
    display_menu_fctn(user)


def display_menu_fctn(user):
    # Affiche un message de bienvenue personnalisé
    print(f"[------------------ Bienvenue {user['name']} ------------------]")
    print("[1] Voir son solde  [2] Retirer de l'argent  [3] Ajouter de l'argent [q] Quitter le programme")
    print('')
    
    # Boucle principale du menu
    while True:
        # L’utilisateur choisit une action
        action = input('Choisissez une action : ')

        # Option 1 : voir le solde
        if action == "1":
            os.system('cls')  # Efface l’écran
            view_sold_fctn(user)  # Appelle la fonction pour voir le solde
            break

        # Option 2 : retirer de l’argent
        elif action == "2":
            os.system('cls')
            pull_money_fctn(user)
            break

        # Option 3 : ajouter de l’argent
        elif action == "3":
            os.system('cls')
            add_money_fctn(user)
            break

        # Option q : quitter le programme
        elif action == "q":
            os.system('cls')
            quit()  # Quitte le programme

        # Si l’utilisateur entre une option invalide
        else:
            os.system('cls')
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")
            break


# Exécution du programme : on lance le menu principal
menu_fctn()
