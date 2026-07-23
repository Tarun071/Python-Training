def fib(limit):
    f=0
    s=1
    while f<=limit:
        yield f
        f,s=s,f+s

limit = int(input())
ob = fib(limit)
for i in ob:
    print(i)