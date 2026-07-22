def perfect_number():
    n=int(input())
    for i in range(1,n):
        if n%i:
            sum+=i
    if sum==n:
        print("Perfect number")
    else:
        print("Not a perfect Number")

perfect_number()