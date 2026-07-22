def reverse_a_number():
    n=int(input("Enter a number : "))
    sum=0
    while n!=0:
        rem=n%10
        sum=sum*10+rem
        
        n=n//10
    print(f"Reversed number : {sum}")
reverse_a_number()