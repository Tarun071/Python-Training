def pattern6():
    rows=int(input("Enter rows : "))
    num=2
    for i in range(2,rows+2):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()
pattern6()