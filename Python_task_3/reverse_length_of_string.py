def reverse_length():
    s=input()
    count=0
    #reverse string 
    print(s[::-1])
    #length of string
    for i in s:
        count+=1
    print(f"length of the string : {count}")
reverse_length()