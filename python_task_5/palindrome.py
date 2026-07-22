def palindrome(str):
    if str==str[::-1]:
        print("It is palindrome")
    else:
        print("Not an palindrome")

s_input=input("Enter a string to check palindrome : ")
palindrome(s_input)