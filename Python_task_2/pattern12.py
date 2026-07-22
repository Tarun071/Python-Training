def pattern12():
    rows=int(input("Enter rows : "))
    for i in range(1,rows+1):
        for j in range(1,i+1):
            if j==i:
                print(j,end="")
            else:
                print(j,end="*")
        print()
pattern12()