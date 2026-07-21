def alphabetical():
    s = input("Enter a string: ")
    print("Alphabetical Order:")
    for ch in sorted(s):
        print(ch)
    print()
    print("Reverse Alphabetical Order:")
    for ch in sorted(s,reverse=True):
        print(ch)
alphabetical()