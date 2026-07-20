def half_series():
    n=int(input("Enter n : "))
    sum=0
    for i in range(n):
        sum=sum+(1/(2**i))
    print(sum)
half_series()