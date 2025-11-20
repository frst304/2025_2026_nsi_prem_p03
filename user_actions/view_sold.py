import os

def view_sold_fctn(user):
    # Affiche le titre de la section
    print("\n╔══════════════════════════════════════════════╗")
    print("║           ✦✧  CONSULTATION DU SOLDE  ✧✦      ║")
    print("╚══════════════════════════════════════════════╝")
    
    # Affiche le nom du titulaire du compte (avec la première lettre en majuscule)
    print(f" Titulaire du compte : {user['name'].title()}                  ")
    
    # Affiche le solde actuel du compte avec deux décimales
    print(f" Solde actuel : {user['balance_account']:.2f} €                  ")
    
    # Ligne de séparation pour une meilleure lisibilité
    print("╚══════════════════════════════════════════════╝\n")
    input("Appuyez sur Entrée pour continuer...")
    os.system('cls')
