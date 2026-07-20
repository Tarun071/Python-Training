def big_digit():
    n=int(input("enter a number : "))
    big=-11
    while n!=0:
        rem=n%10
        if rem>big:
            big=rem
        n=n//10
    print(f"Biggest number : {big}")
big_digit()