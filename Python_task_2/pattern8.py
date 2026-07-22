def pattern8():
    rows=int(input("Enter rows : "))
    for i in range(2,rows+2):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
pattern8()