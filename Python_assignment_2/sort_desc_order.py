def descending_order():
    arr=list(map(int,input("Enter elements : ").split()))
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print(arr)
descending_order()