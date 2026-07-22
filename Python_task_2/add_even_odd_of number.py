def add_even_odd_digits():
    n=int(input("Enter the number : "))
    even_sum=0
    odd_sum=0
    while n!=0:
        rem=n%10
        if rem%2==0:
            even_sum+=rem
        else:
            odd_sum+=rem
        n=n//10
    print(f"Even sum : {even_sum}")
    print(f"Odd sum : {odd_sum}")
add_even_odd_digits()