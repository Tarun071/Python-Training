def perfect_between():
    m=int(input("Enter starting number : "))
    n=int(input("Enter ending number : "))
    for i in range(m,n+1):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            print(i)
perfect_between()