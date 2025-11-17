import json
import os

def create_acount_fctn():
    # Efface l'écran (fonctionne sous Windows)
    os.system('cls')
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                 ✦✧  Création de votre compte  ✧✦                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝")

    # --- Lecture du fichier JSON (chargement des utilisateurs existants) ---
    try:
        with open('data_users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    # Demande du nom complet
    name = input("Entrez votre nom complet : ").strip().lower()

    # --- Saisie de l'âge avec vérification ---
    while True:
        try:
            age = int(input("Entrez votre âge : "))
            if age <= 0:
                print("❌ L'âge doit être un nombre positif.")
            elif age < 10:
                print("⚠️ Vous devez avoir au moins 10 ans pour créer un compte.")
            else:
                break  # âge valide → on sort de la boucle
        except ValueError:
            print("⚠️ Veuillez entrer un nombre entier valide pour l'âge.")

    # Création automatique de l'identifiant
    username = name.split()[0][0] + "." + name.split()[-1]

    # Vérifie si cet identifiant existe déjà
    for user in users:
        if user['id'] == username:
            print(f"❌ L'identifiant '{username}' existe déjà. Veuillez réessayer.")
            return None

    # Saisie du mot de passe
    password = input("Choisissez un mot de passe : ").strip()

    # Création du nouvel utilisateur
    new_user = {
        'id': username,
        'password': password,
        'name': name,
        'age': age,
        'balance_account': 0.0
    }

    # Ajout à la liste et sauvegarde
    users.append(new_user)

    with open('data_users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

    # Confirmation
    print(f"✅ Compte créé avec succès ! Votre identifiant est : {username}")

    input("Appuyez sur Entrée pour continuer...")

    return new_user
