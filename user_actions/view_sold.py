from display_menu import display_menu_fctn

def view_sold_fctn(user):

    print(f'Votre solde est de {user["balance_account"]}')
    display_menu_fctn(user)
    pass