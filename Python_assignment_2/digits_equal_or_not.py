def equal_digits():
    n=int(input("Enter a number : "))
    digit=n%10
    flag=True
    while n!=0:
        rem=n%10
        if rem!=digit:
            flag=False
            break
        n=n//10
    if flag:
        print("Equal")
    else:
        print("Not Equal")
equal_digits()