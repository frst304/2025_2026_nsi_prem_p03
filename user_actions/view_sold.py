from menu import display_menu

def view_sold_fctn(user):

    print(f'Votre solde est de {user["balance_account"]}')
    display_menu(user)
    pass