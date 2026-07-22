def username_checker():
    users_list=["alluarjun","pawankalyan123","tinte321","tarun123"]
    username=input().lower()
    if username in users_list:
        print("Username already taken")
    else:
        users_list.append(username)
        print("Username created")
username_checker()