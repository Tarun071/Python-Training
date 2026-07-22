def copy_array():
    array=list(map(int,input().split()))
    dup_array=[]
    for i in array:
        dup_array.append(i)
    print(f"array : {array}")
    print(f"Copy array : {dup_array}")
copy_array()