def sum_array():
    arr=list(map(int,input("Enter elements : ").split()))
    sum=0
    for i in arr:
        sum+=i
    print("Sum :",sum)
sum_array()