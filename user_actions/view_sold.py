def view_sold_fctn(user):
    print("\n=== CONSULTATION DU SOLDE ===")
    print(f"Titulaire du compte : {user['name'].title()}")
    print(f"Solde actuel : {user['balance_account']:.2f} €")
    print("==============================\n")

    return 