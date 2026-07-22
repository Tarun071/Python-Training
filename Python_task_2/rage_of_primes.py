def prime_between():
    m=int(input("Enter starting number : "))
    n=int(input("Enter ending number : "))
    for i in range(m,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)
prime_between()