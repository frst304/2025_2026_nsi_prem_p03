import json

def add_money_fctn(user):
    print("\n--- DÉPÔT D'ARGENT ---")

    try:
        # Demande à l'utilisateur de saisir le montant à déposer
        montant = float(input("Entrez le montant à déposer (€) : "))

        if montant <= 0:
            print("❌ Le montant doit être supérieur à 0.")
            return user  # On ne modifie rien

        # Lecture du fichier JSON existant
        with open('data_users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)

        # On cherche l'utilisateur connecté dans la liste
        for u in users:
            if u['id'] == user['id']:
                # On met à jour le solde dans la liste et dans la variable locale
                u['balance_account'] += montant
                user['balance_account'] = u['balance_account']
                break

        # On réécrit le fichier JSON avec les nouvelles données
        with open('data_users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

        # Confirmation à l’écran
        print(f"✅ Dépôt de {montant:.2f}€ effectué avec succès.")
        print(f"💰 Nouveau solde : {user['balance_account']:.2f}€")
        print("==============================\n")

    except ValueError:
        print("⚠️ Veuillez entrer un montant valide (ex : 50 ou 20.5).")

    return user
