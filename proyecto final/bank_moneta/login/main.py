from bank_moneta.login.repository.login_repository import add_user, authenticate_user, get_users, save_users
from bank_moneta.wallet_app.wallet_app import run_wallet_app

def register_user():
    print("\n--- CREATE NEW USER ---")

    while True:
        full_name = input("Enter full name: ")
        if not full_name:
            print("Full name cannot be empty.")
            continue
        break

    while True:
        email = input("Enter email: ")
        if not email:
            print("Email cannot be empty.")
            continue
        break

    while True:
        birth_date = input("Enter birth date (DD/MM/YYYY): ")
        if not birth_date:
            print("Birth date cannot be empty.")
            continue
        break

    while True:
        gender = input("Enter gender (Male, Female, Prefer not to say): ")
        if not gender:
            print("Gender cannot be empty.")
            continue
        break

    while True:
        username = input("Enter a new username: ")
        if not username:
            print("Username cannot be empty.")
            continue
        break

    while True:
        password = input("Enter a new password: ")
        if not password:
            print("Password cannot be empty.")
            continue
        break

    if add_user(username, password, full_name, email, birth_date, gender):
        print("Sign up completed. ¡User created now you can Log in!")
    input("Pres enter to continue...")

def login_user():
    print("\n--- LOG IN ---")
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    if authenticate_user(username_input, password_input):
        print(f"¡Log in completed! Welcome, {username_input}.")
        run_wallet_app(username_input)
        print("Going to the principal menu...")
    else:
        print("Log in failed. Wrong username or password.")
    input("Presione Enter para continuar...")

def main_menu():
    while True:
        print("\n--- WELCOME ---")
        print("1. Sign up")
        print("2. Log in")
        print("3. Exit")

        opcion = input("Choose an option: ")

        if opcion == '1':
            register_user()
        elif opcion == '2':
            login_user()
        elif opcion == '3':
            print("Exiting...")
            break
        else:
            print("not valid option. Please, choose 1, 2 or 3.")

if __name__ == "__main__":
    main_menu()