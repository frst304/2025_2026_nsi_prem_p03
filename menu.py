import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'user_actions'))

from login import login_fctn
from add_money import add_money_fctn
from pull_money import pull_money_fctn
from view_sold import view_sold_fctn


def menu_fctn():
    user = login_fctn()
    os.system('cls' if os.name == 'nt' else 'clear')
    display_menu_fctn(user)


def display_menu_fctn(user):
    while True:
        print(f"[------------------ Bienvenue {user['name']} ------------------]")
        print("[1] Voir son solde  [2] Retirer de l'argent  [3] Ajouter de l'argent [q] Quitter le programme")
        print('')
        action = input('Choisissez une action : ')

        if action == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            view_sold_fctn(user)

        elif action == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            pull_money_fctn(user)
            

        elif action == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            add_money_fctn(user)

        elif action == "q":
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")


if __name__ == "__main__":
    menu_fctn()
