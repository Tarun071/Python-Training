def largest_smallest():
    arr=list(map(int,input("Enter elements : ").split()))
    largest=arr[0]
    smallest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
    print("Largest Number :",largest)
    print("Smallest Number :",smallest)
largest_smallest()