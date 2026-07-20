def armstrong_numbers(): 
    for i in range(1,1001):
        temp=i
        digits=len(str(i))
        sum=0
        while temp!=0:
            rem=temp%10
            sum+=rem**digits
            temp=temp//10
        if sum==i:
            print(i)
armstrong_numbers()