def sum_of_digits(n):
    if n==0:
        return 0
    rem=n%10
    return rem+sum_of_digits(n//10)
print(sum_of_digits(56763))