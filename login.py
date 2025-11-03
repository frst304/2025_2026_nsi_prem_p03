from data_users import users  # On importe la liste des utilisateurs depuis le fichier data_users.py

def login_fctn():
    # Message d’accueil pour la connexion
    print(f"[------------------ Connection à votre compte ------------------]")
    
    # On demande à l’utilisateur de saisir son identifiant et son mot de passe
    username_input = input('Id : ')
    password_input = input('Mot de passe : ')

    # On parcourt la liste des utilisateurs enregistrés
    for user in users:
        # Si l’identifiant et le mot de passe correspondent à un utilisateur
        if username_input == user['id'] and password_input == user['password']:
            return user  # On renvoie les infos de cet utilisateur (connexion réussie)

    # Si aucune correspondance n’est trouvée, on affiche une erreur
    print("Identifiant ou mot de passe incorrect.")
    quit()  # On arrête le programme