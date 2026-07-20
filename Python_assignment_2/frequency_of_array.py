def frequency():
    arr=list(map(int,input().split()))
    for i in arr:
        if arr.count(i)>0:
            print(i,"=",arr.count(i))
            arr[arr.index(i)]="*"
frequency()