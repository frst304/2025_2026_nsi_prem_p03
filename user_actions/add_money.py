def add_money_fctn(user):
    # Affiche le titre de la section de dépôt d'argent
    print("\n--- DÉPÔT D'ARGENT ---")
    
    try:
        # Demande à l'utilisateur de saisir le montant à déposer
        montant = float(input("Entrez le montant à déposer (€) : "))

        
        # Vérifie que le montant est supérieur à 0
        if montant <= 0:
            print(" Le montant doit être supérieur à 0.")
            return user  # On retourne l'utilisateur sans modification

        # Ajoute le montant déposé au solde de l'utilisateur
        user['balance_account'] += montant

        # Affiche un message de confirmation
        print(f" Dépôt de {montant:.2f}€ effectué avec succès.")
        print(f" Nouveau solde : {user['balance_account']:.2f}€")

    except ValueError:
        # Si l'utilisateur n'entre pas un nombre valide
        print(" Veuillez entrer un montant valide (ex : 50 ou 20.5).")

    return 
