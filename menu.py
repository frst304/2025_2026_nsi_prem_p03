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
from send_money import send_money_fctn

from create_acount import create_acount_fctn


def menu_fctn():
    print("╔══════════════════════════════════════════════╗")
    print("║       ✦✧  D.A.B — Accès Utilisateur ✧✦       ║")
    print("╠══════════════════════════════════════════════╣")
    print("║   1 • Connexion ancien utilisateur           ║")
    print("║   2 • Création nouvel utilisateur            ║")
    print("║   q • Quitter le système                     ║")
    print("╚══════════════════════════════════════════════╝")
    print("")
    choice = input("⮞ Sélectionnez une option : ")

    if choice == "1":
         user = login_fctn()
    elif choice == "2":
         user = create_acount_fctn()
    elif choice == "q":
        os.system('cls')
        print("\n" + "="*50)
        print("           Merci d’avoir utilisé notre DAB")
        print("                  À très bientôt !")
        print("="*50 + "\n")
        quit()  # Quitte le programme

    else:
        print("\n┌" + "─"*50 + "┐")
        print("│ ⚠️  Option invalide. Veuillez choisir 1, 2 ou q.  │")
        print("└" + "─"*50 + "┘\n")
        
        quit()
    # On efface l’écran (fonctionne sur Windows)
    os.system('cls')
    # On affiche le menu principal pour l’utilisateur connecté
    display_menu_fctn(user)


def display_menu_fctn(user):

     # Affiche un message de bienvenue personnalisé
    print("╔══════════════════════════════════════════════════════════════════╗")
    print(f"║ ✦✧  Bienvenue {user['name']} — Distributeur Automatique ✧✦      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print("")

     # Boucle principale du menu
    while True:
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║                     ✦✧  Menu Principal du D.A.B ✧✦               ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║   1 • Voir son solde                                             ║")
        print("║   2 • Retirer de l'argent                                        ║")
        print("║   3 • Ajouter de l'argent                                        ║")
        print("║   4 • Envoyer à un ami                                           ║")
        print("║   q • Quitter le programme                                       ║")
        print("╚══════════════════════════════════════════════════════════════════╝")
        print("")
        # L’utilisateur choisit une action
        action = input('Choisissez une action : ')

        # Option 1 : voir le solde
        if action == "1":
            os.system('cls')  # Efface l’écran
            view_sold_fctn(user)  # Appelle la fonction pour voir le solde

        # Option 2 : retirer de l’argent
        elif action == "2":
            os.system('cls')
            pull_money_fctn(user)

        # Option 3 : ajouter de l’argent
        elif action == "3":
            os.system('cls')
            add_money_fctn(user)
        
        # Option 4 : envoyer de l’argent
        elif action == "4":
            os.system('cls')
            send_money_fctn(user)

        # Option q : quitter le programme
        elif action == "q":
            os.system('cls')
            print("\n" + "="*50)
            print("           Merci d’avoir utilisé notre DAB")
            print("                  À très bientôt !")
            print("="*50 + "\n")
            quit()  # Quitte le programme

        # Si l’utilisateur entre une option invalide
        else:
            os.system('cls')
            print("\n┌" + "─"*60 + "┐")
            print("│    ⚠️  Option invalide. Veuillez choisir 1, 2, 3, 4 ou q.   │")
            print("└" + "─"*60 + "┘\n")


# Exécution du programme : on lance le menu principal
menu_fctn()
