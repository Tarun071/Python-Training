def name_start_with_ch():
    arr=["Tarun","ganesh","naveenth","Pavan","Rohit","tanmay"]
    ch=input()
    for i in range(0,len(arr)):
        k=arr[i][0]
        s=k.lower()
        if ch==s:
            print(arr[i])
name_start_with_ch()