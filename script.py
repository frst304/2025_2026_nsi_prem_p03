users = [
    {
        'id': 'a.michel',
        'password': '1234',
        'name': 'Arthur Michel',
        'age': 37,
        'balance_account': 2340.20
    },
    {
        'id': 'a.dupont',
        'password': '3768',
        'name': 'Alice Dupont',
        'age': 29,
        'balance_account': 4150.75
    },
    {
        'id': 'b.leclerc',
        'password': '9584',
        'name': 'Bernard Leclerc',
        'age': 45,
        'balance_account': 1870.30
    }
]

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