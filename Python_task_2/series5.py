def square_series():
    n=int(input("Enter n : "))
    sum=0
    for i in range(1,n+1):
        sum=sum+(1/(i**2))
    print(sum)
square_series()