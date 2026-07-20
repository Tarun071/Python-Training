def pattern15():
    rows=int(input("Enter rows : "))
    for i in range(1,rows+1):
        for j in range(i-1):
            print("*",end="")
        print(i,end="")
        for j in range(i-1):
            print("*",end="")
        print()
pattern15()