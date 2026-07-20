def pattern13():
    rows=int(input("Enter rows : "))
    for i in range(1,rows+1):
        ch=65
        for j in range(i):
            print(chr(ch),end=" ")
            ch+=1
        print()
pattern13()