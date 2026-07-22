def pattern14():
    rows=int(input("Enter rows : "))
    for i in range(rows,0,-1):
        ch=65
        for j in range(i):
            print(chr(ch),end=" ")
            ch+=1
        print()
pattern14()