def list_user():
    response = login_service.list_users()
    print ("id\t name \t email")
    for id, user in enumerate(response["data"]):
        print(f"{id}" + "\t" + user["name"] + "\t" + user ["email"])