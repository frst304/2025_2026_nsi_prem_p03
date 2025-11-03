import sys
import os


from data_users import users

def create_acount_fctn():
    os.system('cls')
    name = input("Entrez votre nom complet : ").strip().lower()
    age = int(input("Entrez votre âge : "))
    username = name.split()[0][0] + "." + name.split()[-1]
    password = input("Choisissez un mot de passe : ").strip()
    user = {
        'id': username,
        'password': password,
        'name': name,
        'age': age,
        'balance_account': 0.0
    }
    users.append(user)
    print(f"Compte créé avec succès. Votre identifiant est : {username}")
    input("Appuyez sur Entrée pour continuer...")
    return user