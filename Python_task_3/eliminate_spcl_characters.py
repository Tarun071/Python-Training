def eliminate():
    s = input("Enter a string: ")
    result = ""
    for ch in s:
        if ch.isalpha():
            result += ch
    print(result)
eliminate()