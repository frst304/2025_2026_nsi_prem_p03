def pull_money_fctn(user):
    # Affiche le titre de la section de retrait
    print("\n=== Retrait d'argent ===")
    
    try:
        # Demande à l'utilisateur de saisir le montant à retirer
        montant = float(input("Entrez le montant à retirer (€) : "))
    except ValueError:
        # Si la saisie n'est pas un nombre, message d'erreur
        print("Montant invalide.")
        return

    # Vérifie que le montant est positif
    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
        return

    # Vérifie que l'utilisateur a assez d'argent sur son compte
    if montant > user['balance_account']:
        print(f"Solde insuffisant. Solde actuel : {user['balance_account']:.2f} €.")
        return

    # Vérifie que le montant est un multiple de 5 (car les billets sont de 5€ minimum)
    if montant % 5 != 0:
        print("Le montant doit être un multiple de 5 € (billets : 50, 20, 10, 5).")
        return

    # Liste des billets disponibles
    billets = [50, 20, 10, 5]
    # Dictionnaire pour stocker la décomposition du montant en billets
    decomposition = {}
    # Reste du montant à décomposer
    reste = montant

    # Calcul de la décomposition en billets
    for billet in billets:
        nb_billets = int(reste // billet)  # Nombre de billets de ce type
        if nb_billets > 0:
            decomposition[billet] = nb_billets  # Enregistre le nombre de billets
            reste -= nb_billets * billet        # Met à jour le reste à retirer

    # Mise à jour du solde de l'utilisateur
    user['balance_account'] -= montant

    # Affichage du résumé de l’opération
    print("\nRetrait effectué !")
    print(f"Montant retiré : {montant:.2f} €")
    print("Détails des billets :")
    for billet, nb in decomposition.items():
        print(f"  - {nb} billet(s) de {billet} €")
    
    # Affiche le nouveau solde après retrait
    print(f"\nNouveau solde : {user['balance_account']:.2f} €")

