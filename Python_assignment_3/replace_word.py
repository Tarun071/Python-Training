def replace_first_letter():
    s = input("Enter a string: ")
    words = s.split()
    result = ""
    for word in words:
        first = chr(ord(word[0]) - 1)
        result += first + word[1:] + " "
    print(result)
replace_first_letter()