import json
import os

DATA_FILE = "data_users.json"

# ======================================================
#  LECTURE / ÉCRITURE DU FICHIER JSON
# ======================================================

def load_users():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


# ======================================================
#  FONCTION : CHANGEMENT DE MOT DE PASSE
# ======================================================

def change_password(user):
    users = load_users()

    print("\n--- Changement de mot de passe ---")
    old = input("Ancien mot de passe : ")

    if old != user["password"]:
        print("❌ Mot de passe incorrect.")
        return user

    new = input("Nouveau mot de passe : ")
    confirm = input("Confirmez le mot de passe : ")

    if new != confirm:
        print("❌ Les mots de passe ne correspondent pas.")
        return user

    # Mise à jour dans user_data.json
    for u in users:
        if u["id"] == user["id"]:
            u["password"] = new
            user["password"] = new
            break

    save_users(users)
    print("✔ Mot de passe mis à jour !")
    return user


# ======================================================
#  FONCTION : CHANGEMENT D'IDENTIFIANT (ID)
# ======================================================

def change_username(user):
    users = load_users()

    print("\n--- Changement de nom d'utilisateur ---")
    new_id = input("Nouvel identifiant : ")

    # Vérifie si déjà existant
    if any(u["id"] == new_id for u in users):
        print("❌ Cet identifiant existe déjà.")
        return user

    # Mise à jour
    for u in users:
        if u["id"] == user["id"]:
            u["id"] = new_id
            user["id"] = new_id
            break

    save_users(users)
    print("✔ Identifiant mis à jour !")
    return user


# ======================================================
#  FONCTION : SUPPRESSION DU COMPTE
# ======================================================

def delete_account(user):
    users = load_users()

    print("\n--- Suppression du compte ---")
    confirm = input("Êtes-vous sûr de vouloir supprimer votre compte ? (oui/non) : ")

    if confirm.lower() != "oui":
        print("❌ Suppression annulée.")
        return user

    # Suppression de l'utilisateur
    users = [u for u in users if u["id"] != user["id"]]
    save_users(users)

    print("✔ Votre compte a bien été supprimé.")
    return None  # Aucun utilisateur (déconnexion)


# ======================================================
#  MENU DES PARAMÈTRES
# ======================================================

def settings_fctn(user):
    print("╔══════════════════════════════════════════════╗")
    print("║         ✦✧  Parametre du compte ✧✦           ║")
    print("╠══════════════════════════════════════════════╣")
    print("║   1 • Modification de mot de passe           ║")
    print("║   2 • Modification de nom d'utilisateur      ║")
    print("║   3 • Suppression du compte                  ║")
    print("║   q • Retour                                 ║")
    print("╚══════════════════════════════════════════════╝")
    print("")

    choice = input("⮞ Sélectionnez une option : ")

    if choice == "1":
        change_password(user)
        input("Appuyez sur Entrée pour continuer...")
        os.system('cls')
        return user

    elif choice == "2":
        change_username(user)
        input("Appuyez sur Entrée pour continuer...")
        os.system('cls')
        return user

    elif choice == "3":
        delete_account(user)
        input("Appuyez sur Entrée pour continuer...")
        os.system('cls')
        quit()

    elif choice == "q":
        os.system('cls')
        return user
    
    else:
        os.system('cls')
        print("\n┌" + "─"*60 + "┐")
        print("│    ⚠️  Option invalide. Veuillez choisir 1, 2, 3 ou q.   │")
        print("└" + "─"*60 + "┘\n")
