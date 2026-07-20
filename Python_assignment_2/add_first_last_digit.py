def add_first_last_digit():
    n=int(input("Enter the number : "))
    last_number=n%10
    while n<=10:
        n=n//10
    first_number=n
    print(f"sum of first and last number : {first_number+last_number}")
add_first_last_digit()