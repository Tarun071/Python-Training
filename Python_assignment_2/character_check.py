def Character_check():
    ch=input()

    if ch>='A' and ch<='Z':
        print("Uppercase")
    elif ch>='a' and ch<='z':
        print("Lowercase")
    elif ch>='0' and ch<='9':
        print("Digit")
    else:
        print("Special Character")

Character_check()