def replace_substring():
    s = input("Enter a string: ")
    old = input("Enter substring to replace: ")
    new = input("Enter new substring: ")
    s = s.replace(old, new)
    print("Modified String:", s)
replace_substring()