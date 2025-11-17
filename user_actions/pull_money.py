import json

def pull_money_fctn(user):
    # Affiche le titre de la section de retrait
    print("\n╔══════════════════════════════════════════════╗")
    print("║              ✦✧  RETRAIT D'ARGENT  ✧✦        ║")
    print("╚══════════════════════════════════════════════╝")


    try:
        # Demande à l'utilisateur de saisir le montant à retirer
        montant = float(input("Entrez le montant à retirer (€) : "))
    except ValueError:
        print("⚠️ Montant invalide.")
        return user

    # Vérifie que le montant est positif
    if montant <= 0:
        print("❌ Le montant doit être supérieur à 0.")
        return user

    # Vérifie que l'utilisateur a assez d'argent sur son compte
    if montant > user['balance_account']:
        print(f"💸 Solde insuffisant. Solde actuel : {user['balance_account']:.2f} €.")
        return user

    # Vérifie que le montant est un multiple de 5 (billets disponibles)
    if montant % 5 != 0:
        print("⚠️ Le montant doit être un multiple de 5 € (billets : 50, 20, 10, 5).")
        return user

    # Liste des billets disponibles
    billets = [50, 20, 10, 5]
    decomposition = {}
    reste = montant

    # Décomposition du montant en billets
    for billet in billets:
        nb_billets = int(reste // billet)
        if nb_billets > 0:
            decomposition[billet] = nb_billets
            reste -= nb_billets * billet

    # Mise à jour du solde en mémoire
    user['balance_account'] -= montant

    # --- Mise à jour du fichier JSON ---
    try:
        with open('data_users.json', 'r', encoding='utf-8') as file:
            users = json.load(file)

        # Trouver l'utilisateur et mettre à jour son solde
        for u in users:
            if u['id'] == user['id']:
                u['balance_account'] = user['balance_account']
                break

        # Réécrire le fichier JSON
        with open('data_users.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

    except FileNotFoundError:
        print("❌ Erreur : fichier 'data_users.json' introuvable. Impossible d'enregistrer la modification.")

    # --- Affichage du résumé ---
    print("\n✅ Retrait effectué !")
    print("╔══════════════════════════════════════════════╗")
    print(f"║   💰 Montant retiré : {montant:.2f} €                        ║")
    print("║   💵 Détails des billets :                                   ║")
    for billet, nb in decomposition.items():
        print(f"║     - {nb} billet(s) de {billet} €                               ║")
    print(f"║                                                          ")
    print(f"║   💳 Nouveau solde : {user['balance_account']:.2f} €             ║")
    print("╚══════════════════════════════════════════════╝\n")

    return user
