def happy_number():
    num=int(input("Enter number : "))
    temp=num
    while temp!=1 and temp!=4:
        sum=0
        while temp>0:
            digit=temp%10
            sum=sum+(digit**2)
            temp=temp//10
        temp=sum
    if temp==1:
        print("Happy Number")
    else:
        print("Not a Happy Number")
happy_number()