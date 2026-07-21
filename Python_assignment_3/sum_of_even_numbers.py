def sum_of_even():
    arr=list(map(int,input().split()))
    sum=0
    for i in arr:
        if i%2==0:
            sum+=i
    print(f"Sum of even numbers : {sum}")

sum_of_even()