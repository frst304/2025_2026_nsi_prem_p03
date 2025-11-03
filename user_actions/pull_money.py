def pull_money_fctn(user):
    print("\n=== Retrait d'argent ===")
    try:
        montant = float(input("Entrez le montant à retirer (€) : "))
    except ValueError:
        print("Montant invalide.")
        return

    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
        return

    if montant > user['balance_account']:
        print(f"Solde insuffisant. Solde actuel : {user['balance_account']:.2f} €.")
        return

    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 € (billets : 50, 20, 10, 5).")
        return

    billets = [50, 20, 10, 5]
    decomposition = {}
    reste = montant

    for billet in billets:
        nb_billets = int(reste // billet)
        if nb_billets > 0:
            decomposition[billet] = nb_billets
            reste -= nb_billets * billet

    user['balance_account'] -= montant

    print("\nRetrait effectué !")
    print(f"Montant retiré : {montant:.2f} €")
    print("Détails des billets :")
    for billet, nb in decomposition.items():
        print(f"  - {nb} billet(s) de {billet} €")
    print(f"\nNouveau solde : {user['balance_account']:.2f} €")

    return 