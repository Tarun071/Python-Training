def pattern3():
    rows=int(input("Enter rows : "))
    for i in range(1,rows+1):
        for j in range(i):
            print("*",end="")
        print()
pattern3()