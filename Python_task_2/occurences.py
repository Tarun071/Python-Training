def digit_occurrences():
    n=int(input("Enter a number : "))
    digit=int(input("Enter digit : "))
    count=0
    while n!=0:
        rem=n%10
        if rem==digit:
            count+=1
        n=n//10
    print(count)
digit_occurrences()