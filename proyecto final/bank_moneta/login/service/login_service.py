from login.repository import login_repository
from login.exceptions import login_exceptions

def login(email,password):
    users = login_repository.get_users()
    response = {}
    try:
        for user in users:
            if user["email"] == email:
                if user["password"] == password:
                    response["status_code"] = 200
                    response["message"] = "user exist"
                    response["user"] = user
                else:
                    raise login_exceptions.NotFound()
        return response
    except login_exceptions.NotFound as ex:
        response= {}
        response["message"] = "Wrong password"
        response["status_code"]= 400
        return response
    
def register(name,email,password):
    users = login_repository.get_users()
    exists= list(filter(lambda user: user["email"]== email,users))
    if exists:
        response = {}
        response["message"] = "That email already exists"
        response["status_code"] = 400
        return response
    users.append({
        "name":name,
        "email": email,
        "password": password
    })
    response = {}
    response["status_code"] = 200
    response ["user"] = users[-1]
    login_repository.save_users(users)
    return response

def list_users():
   users = login_repository.get_users()
   users = list(map(lambda user: {"name" : user ["name"], "email" : user ["email"]}))

   response = {}
   response["data"] = users 
   response["status_code"] = 200
   return response 
