

def data_saving(name, email, born_date, gender, password):
    new_user = []           
    users = []   
  

def main():
    while True:
        name = input("Enter your full name: ")
        email = input("Enter your email: ")
        born_date = input("Enter your birth date (YYYY-MM-DD): ")
        gender = input("Enter your gender: ")
        password = input("Create a password: ")

        user = data_saving(name, email, born_date, gender, password)
        user.append(user)

























    username = (
        name.lower().split()[0] +  # Primera parte del nombre en minúsculas
        born_date.split("-")[0] +  # Año de nacimiento
        gender[0].lower()          # Primera letra del género
    )

    # 3. Almacenar en la lista
    users.append(username)

    # 4. Mostrar resultados
    print(f"\n✅ Usuario registrado: {username}")
    print(f"📋 Lista actual: {users}")

    # 5. Retornar el username (como en tu código original)
    return username


































    # 2. Generar username (ej: "ana2005f")
    username = (
        name.lower().split()[0] +  # Primera parte del nombre
        born_date.split("-")[0] +  # Año de nacimiento
        gender[0].lower()          # Primera letra del género
    )

    # 3. Almacenar en lista
    users.append(username)

    # 4. Mostrar resultados
    print(f"\nUsername generado: {username}")
    print(f"Lista actual: {users}")

    # 5. Retornar el username (como en tu código original)
    return username

# Llamar a la función
register_username()