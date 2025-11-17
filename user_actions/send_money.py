import json

def send_money_fctn(user):
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║           ✦✧  ENVOI D'ARGENT À UN UTILISATEUR  ✧✦       ║")
    print("╚══════════════════════════════════════════════════════════╝")


    try:
        # Nom ou ID du destinataire
        receiver_id = input("Entrez l'ID de l'utilisateur à qui envoyer : ").strip()

        # Montant à envoyer
        montant = float(input("Entrez le montant à envoyer (€) : "))
        if montant <= 0:
            print("❌ Le montant doit être supérieur à 0.")
            return user

        # Lecture des comptes
        with open('data_users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)

        # Recherche du destinataire
        receiver = None
        for u in users:
            if str(u['id']) == receiver_id:
                receiver = u
                break

        if receiver is None:
            print("❌ Aucun utilisateur trouvé avec cet ID.")
            return user

        # Vérification du solde
        if user['balance_account'] < montant:
            print("❌ Solde insuffisant pour effectuer ce transfert.")
            return user

        # Déduction chez l'envoyeur
        for u in users:
            if u['id'] == user['id']:
                u['balance_account'] -= montant
                user['balance_account'] = u['balance_account']  # mise à jour du user
                break

        # Ajout chez le destinataire
        receiver['balance_account'] += montant

        # Sauvegarde dans le fichier
        with open('data_users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

        # Confirmation
        print("╔══════════════════════════════════════════════════════╗")
        print(f"   ✅ Vous avez envoyé {montant:.2f} € à l'utilisateur {receiver_id}.      ")
        print(f"  💰 Nouveau solde : {user['balance_account']:.2f} €                    ")
        print("╚══════════════════════════════════════════════════════╝\n")

    except ValueError:
        print("⚠️ Veuillez entrer un montant valide (ex : 50 ou 20.5).")

    return user