def infinite_prime():
    n=2
    while n>0:
        n+=1
        count=0
        for i in range(2,n):
            if i%n==0:
                count+=1
        if count==0:
#             yield n
# ob=infinite_prime()
# for i in ob:
#     print(i)