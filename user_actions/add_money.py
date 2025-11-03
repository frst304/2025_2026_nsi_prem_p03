def add_money_fctn(user):
    
    print("\n=== Depot d'argent ===")
    
    try:
        montant = float(input("Entrez le montant à ajouter (€) : "))
        
        if montant <= 0:
            print(" Le montant doit être supérieur à 0.")
            return user

        user['balance_account'] += montant
        print(f"Dépôt de {montant:.2f}€ effectué avec succès.")
        print(f"Nouveau solde : {user['balance_account']:.2f}€")

    except ValueError:
        print(" Veuillez entrer un montant valide (ex : 50 ou 20.5).")

    return 
