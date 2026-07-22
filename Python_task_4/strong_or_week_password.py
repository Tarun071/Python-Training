def password_validation():
    password = input("Enter Password: ")
    upper = lower = digit = special = 0
    if len(password) < 8:
        print("Weak Password")
        return
    for i in password:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        else:
            special += 1
    if upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        print("Strong Password")
    else:
        print("Weak Password")
password_validation()