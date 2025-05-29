import json
from bank_moneta.login.repository.login_repository import get_users, save_users

current_user_balance = 0
current_user_history = []
current_active_username = None
current_user_categories = []

DEFAULT_CATEGORIES = [
    "Transportation",
    "Food",
    "Housing",
    "Entertainment",
    "Education",
    "Health",
    "Beauty",
    "Clothing",
    "Gifts",
    "Salary",
    "Investment",
    "Others"
]

def menu():
    print("\n---- Main Menu (Wallet App) ----")
    print("1. Current Balance")
    print("2. Add Record (Income/Expense)")
    print("3. History")
    print("4. Manage Categories")
    print("5. Exit Wallet App")

def show_balance():
    global current_user_balance
    print(f"Current Balance: {current_user_balance}")
    input("Press Enter to continue...")

def display_all_categories():
    global current_user_categories
    print("\n--- Available Categories ---")
    if not current_user_categories:
        print("No categories defined. Please add some!")
        return False
    for i, category in enumerate(current_user_categories):
        print(f"{i+1}. {category}")
    return True

def movements():
    global current_user_balance
    global current_user_history
    global current_user_categories

    print("Pick a movement (write the number)")
    movement = input(" --1. Income-- " \
                     "--2. Expense-- ")

    print("Movement selected: ", movement)

    if movement == '1' or movement == '2':
        while True:
            try:
                amount = float(input(f"How much money ({'income' if movement == '1' else 'expense'}): "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        if not display_all_categories():
            print("Cannot add record without categories. Please add categories first.")
            input("Press Enter to continue...")
            return False

        while True:
            try:
                category_choice = int(input("Enter category number: "))
                if 1 <= category_choice <= len(current_user_categories):
                    selected_category = current_user_categories[category_choice - 1]
                    break
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        fecha = input("Enter the date (D/M/Y): ")
        
        if movement == '1':
            current_user_balance += amount
            current_user_history.append({"fecha": fecha, "tipo": "Income", "monto": amount, "categoria": selected_category})
            print(f"Income of {amount} ({selected_category}) added. New Balance: {current_user_balance}")
        else:
            current_user_balance -= amount
            current_user_history.append({"fecha": fecha, "tipo": "Expense", "monto": -amount, "categoria": selected_category})
            print(f"Expense of {amount} ({selected_category}) added. New Balance: {current_user_balance}")

    else:
        print("Invalid option selected.")

    return True

def show_history():
    global current_user_history
    print("Transaction History:")
    if not current_user_history:
        print("No transactions recorded yet.")
    else:
        for record in current_user_history:
            category_info = f" ({record['categoria']})" if 'categoria' in record else ""
            print(f"{record['fecha']} - {record['tipo']}{category_info}: {record['monto']}")
    input("Press Enter to continue...")

def manage_categories():
    global current_user_categories
    global current_active_username

    print("\n--- Manage Categories ---")
    print("1. View My Categories")
    print("2. Add New Category")
    print("3. Back to Wallet Menu")

    manage_option = input("Select an option: ")

    if manage_option == '1':
        display_all_categories()
        input("Press Enter to continue...")
    elif manage_option == '2':
        new_category = input("Enter the name for the new category: ").strip()
        if not new_category:
            print("Category name cannot be empty.")
            input("Press Enter to continue...")
            return

        if new_category.lower() in [cat.lower() for cat in current_user_categories]:
            print(f"Category '{new_category}' already exists. Please choose a different name.")
            input("Press Enter to continue...")
            return
        
        current_user_categories.append(new_category)
        print(f"Category '{new_category}' added successfully!")

        all_users_data = get_users()
        user_data = all_users_data.get(current_active_username, {})
        if "custom_categories" not in user_data or not isinstance(user_data["custom_categories"], list):
            user_data["custom_categories"] = []
        user_data["custom_categories"].append(new_category)
        all_users_data[current_active_username] = user_data
        save_users(all_users_data)

        input("Press Enter to continue...")
    elif manage_option == '3':
        print("Returning to Wallet Menu.")
    else:
        print("Invalid option selected.")
        input("Press Enter to continue...")

def run_wallet_app(username):
    global current_user_balance
    global current_user_history
    global current_active_username
    global current_user_categories

    current_active_username = username

    all_users_data = get_users()
    user_data = all_users_data.get(current_active_username, {})

    current_user_balance = user_data.get("wallet_balance", 0)
    
    loaded_history = user_data.get("wallet_history", [])
    current_user_history = []
    for record in loaded_history:
        if 'categoria' not in record:
            record['categoria'] = 'N/A'
        current_user_history.append(record)

    loaded_custom_categories = user_data.get("custom_categories", [])
    current_user_categories = DEFAULT_CATEGORIES + loaded_custom_categories
    current_user_categories = sorted(list(set(current_user_categories)))


    print(f"\nWelcome to Wallet App, {current_active_username}!")
    running_wallet = True
    while running_wallet:
        menu()
        option = input("Select an option (write the number): ")

        if option == '1':
            show_balance()
        elif option == '2':
            movements()
            input("Press Enter to continue...")
        elif option == '3':
            show_history()
        elif option == '4':
            manage_categories()
        elif option == '5':
            running_wallet = False
            print("Exiting Wallet App. Goodbye!")
        else:
            print("Invalid option selected.")
            input("Press Enter to continue...")

    all_users_data = get_users()
    all_users_data[current_active_username]["custom_categories"] = [
        cat for cat in current_user_categories if cat not in DEFAULT_CATEGORIES
    ]
    all_users_data[current_active_username]["wallet_balance"] = current_user_balance
    all_users_data[current_active_username]["wallet_history"] = current_user_history
    save_users(all_users_data)