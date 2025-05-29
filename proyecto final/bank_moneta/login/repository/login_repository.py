import os
import json
from ..constants.login_constants import USER_FILE

def ensure_file_and_directory_exist():
    directory = os.path.dirname(USER_FILE)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(USER_FILE) or os.stat(USER_FILE).st_size == 0:
        with open(USER_FILE, 'w') as f:
            json.dump({}, f)

def get_users():
    ensure_file_and_directory_exist()
    try:
        with open(USER_FILE, 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                data = {}
                save_users(data)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        data = {}
        save_users(data)
        return data
    except Exception:
        data = {}
        save_users(data)
        return data

def save_users(users):
    ensure_file_and_directory_exist()
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def add_user(username, password, full_name, email, birth_date, gender):
    users = get_users()
    if username in users:
        print("Error: Username already exists.")
        return False
    
    users[username] = {
        "password": password,
        "full_name": full_name,
        "email": email,
        "birth_date": birth_date,
        "gender": gender,
        "wallet_balance": 0,
        "wallet_history": [],
        "custom_categories": []
    }
    save_users(users)
    return True

def authenticate_user(username, password):
    users = get_users()
    if username not in users:
        return False
    
    return users[username]["password"] == password