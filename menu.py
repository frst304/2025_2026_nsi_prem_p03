import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'user_actions'))

from login import login_fctn

from create_acount import create_acount_fctn


def menu_fctn():
    print("[------------------ Bienvenue ------------------]")
    print("[1] Ancien utilisateur  [2] Nouvel utilisateur  [q] Quitter le programme")
    print('')
    choice = input('Choisissez une action : ')

    if choice == "1":
         user = login_fctn()
    elif choice == "2":
         user = create_acount_fctn()
    else:
         print("Option invalide. Veuillez choisir 1 ou 2.")
         quit()

    os.system('cls')
    display_menu_fctn(user)

def display_menu_fctn(user):

        print(f"[------------------ Bienvenue {user['name']} ------------------]")
        print("[1] Voir son solde  [2] Retirer de l'argent  [3] Ajouter de l'argent [q] Quitter le programme")
        print('')
        
        while True:
            action = input('Choisissez une action : ')

            if action == "1":
                os.system('cls')
                view_sold_fctn(user)
                break

            elif action == "2":
                os.system('cls')
                pull_money_fctn(user)
                break

            elif action == "3":
                os.system('cls')
                add_money_fctn(user)
                break

            
            elif action == "q":
                os.system('cls')
                quit() 
            
            else:
                os.system('cls')
                print("Option invalide. Veuillez choisir 1, 2 ou 3.")
                break

menu_fctn()