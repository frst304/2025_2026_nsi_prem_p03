from data_users import users

def login_fctn():
    username_input = input('Id : ')
    password_input = input('Mot de passe : ')

    for user in users:
        if username_input == user['id'] and password_input == user['password']:
            return user

    print("Identifiant ou mot de passe incorrect.")
    quit()