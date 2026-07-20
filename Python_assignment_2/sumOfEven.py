def sum_of_even():
    n=int(input("Enter a range : "))
    sum=0
    for i in range(1,n+1):
        sum+=(i*2)
    print(f"Sum : {sum}")
sum_of_even()