from login import login_fctn
import os

def menu():
    user = login_fctn()
    os.system('cls')
    print(f'[------------------ Bienvenue {login_fctn.user['name']} ------------------]')
    print('')
