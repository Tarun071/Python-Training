def pattern7():
    rows=int(input("Enter rows : "))
    for i in range(2,rows+2):
        num=5
        for j in range(i):
            print(num,end=" ")
            num-=1
        print()
pattern7()