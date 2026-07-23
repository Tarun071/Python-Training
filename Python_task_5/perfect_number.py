def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if n==sum:
        return "It is a perfect number"
    else:
        return "It is not an perfect number"
number=int(input("Enter a number : "))
print(perfect_number(number))
