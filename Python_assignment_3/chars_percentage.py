def percentage():
    s = input("Enter a string: ")
    upper = lower = vowels = consonants = digits = special = 0
    total = len(s)
    for ch in s:
        if ch.isupper():
            upper += 1
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif ch.islower():
            lower += 1
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1
    print("Uppercase:",upper*100/total)
    print("Lowercase:",lower*100/total)
    print("Vowels:",vowels*100/total)
    print("Consonants:",consonants*100/total)
    print("Digits:",digits*100/total)
    print("Special Chars:",special*100/total)
percentage()