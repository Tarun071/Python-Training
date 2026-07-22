def n_even():
    n=int(input("Enter the number : " ))
    temp=0
    count=0
    while count==n+1:
        if temp%2==0:
            print(temp)
        temp+=2
n_even()