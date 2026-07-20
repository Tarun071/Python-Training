def alternative_digit_sum():
    n=int(input("Enter a number : "))
    sum=0
    flag=0
    while n!=0:
        rem=n%10
        if flag==0:
            sum+=rem
            flag=1
        else:
            flag=0
        n=n//10
    print(sum)
alternative_digit_sum()