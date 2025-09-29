from data_users import users

def login():
    username_input = input('Id : ')
    password_input = input('Mot de passe : ')

    for user in users:
        if username_input == user['id'] and password_input == user['password']:
            print(f"Bienvenue {user['name']}! Vous êtes connecté.")
            return

    print("Identifiant ou mot de passe incorrect.")

    return None

def account_system():
    pass

def main():
    login()


main()