import json
import os

def create_acount_fctn():
    # Efface l'écran (fonctionne sous Windows)
    os.system('cls')

    # --- Lecture du fichier JSON (chargement des utilisateurs existants) ---
    try:
        with open('data_users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        # Si le fichier n'existe pas encore, on crée une liste vide
        users = []

    # Demande à l'utilisateur de saisir son nom complet
    name = input("Entrez votre nom complet : ").strip().lower()

    # Demande à l'utilisateur de saisir son âge
    age = int(input("Entrez votre âge : "))

    # Crée un identifiant automatique à partir du prénom et du nom
    username = name.split()[0][0] + "." + name.split()[-1]

    # Vérifie si cet identifiant existe déjà
    for user in users:
        if user['id'] == username:
            print(f"❌ L'identifiant '{username}' existe déjà. Veuillez réessayer.")
            return None

    # Demande à l'utilisateur de choisir un mot de passe
    password = input("Choisissez un mot de passe : ").strip()

    # Crée un dictionnaire pour le nouvel utilisateur
    new_user = {
        'id': username,
        'password': password,
        'name': name,
        'age': age,
        'balance_account': 0.0
    }

    # Ajoute le nouvel utilisateur à la liste
    users.append(new_user)

    # --- Enregistre la nouvelle liste dans le fichier JSON ---
    with open('data_users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

    # Message de confirmation
    print(f"✅ Compte créé avec succès ! Votre identifiant est : {username}")

    # Pause avant de continuer
    input("Appuyez sur Entrée pour continuer...")

    # Retourne les informations du nouvel utilisateur
    return new_user
