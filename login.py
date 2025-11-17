import json  # Pour lire les fichiers JSON
import os

def login_fctn():
    # Lecture du fichier JSON
    with open('data_users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)  # On charge la liste des utilisateurs depuis le JSON
    
    # Efface l'écran (fonctionne sous Windows)
    os.system('cls')

    # Message d’accueil pour la connexion
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                 ✦✧  Connexion à votre compte  ✧✦                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    
    # On demande à l’utilisateur de saisir son identifiant et son mot de passe
    username_input = input('Id : ')
    password_input = input('Mot de passe : ')

    # On parcourt la liste des utilisateurs enregistrés
    for user in users:
        # Si l’identifiant et le mot de passe correspondent à un utilisateur
        if username_input == user['id'] and password_input == user['password']:
            return user  # Connexion réussie → on renvoie les infos de l’utilisateur

    # Si aucune correspondance n’est trouvée, on affiche une erreur
    print("Identifiant ou mot de passe incorrect.")
    quit()  # On arrête le programme
