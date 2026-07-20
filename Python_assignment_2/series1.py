def series():
    n=int(input("Enter n : "))
    sum=0
    for i in range(1,n+1):
        sum=sum+(1/i)
    print(sum)
series()