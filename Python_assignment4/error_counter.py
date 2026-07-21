def error_counter():
    error_log=input().split()
    count=0
    for i in error_log:
        if i.lower()=="error":
            count+=1
    print(f"Error count : {count}")
error_counter()