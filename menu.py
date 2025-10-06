import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'user_actions'))

from login import login_fctn
from view_sold import view_sold_fctn # type: ignore
from pull_money import pull_money_fctn # type: ignore
from add_money import add_money_fctn # type: ignore

def menu():
    user = login_fctn()
    os.system('cls')
    print(f"[------------------ Bienvenue {user['name']} ------------------]")
    print("[1] Voir son solde  [2] Retirer de l'argent  [3] Ajouter de l'argent [q] Quitter le programme")
    print('')
    
    while True:
        action = input('Choisissez une action : ')

        if action == "1":
            os.system('cls')
            view_sold_fctn()
            break

        elif action == "2":
            os.system('cls')
            pull_money_fctn()
            break

        elif action == "3":
            os.system('cls')
            add_money_fctn()
            break

        
        elif action == "q":
            os.system('cls')
            quit() 
        
        else:
            os.system('cls')
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")
            menu()
