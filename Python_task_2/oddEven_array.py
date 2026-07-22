def odd_even():
    arr=list(map(int,input("Enter elements : ").split()))
    print("Even Numbers")
    for i in arr:
        if i%2==0:
            print(i)
    print("Odd Numbers")
    for i in arr:
        if i%2!=0:
            print(i)
odd_even()