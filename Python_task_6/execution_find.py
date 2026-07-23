import time
def dec(fun):
    def wrapper():
        start=time.perf_counter()
        fun()
        end=time.perf_counter()
        print(end)
    return wrapper

@dec 
def add():
    sum=0
    m=[10,10,10,20]
    for i in m:
        sum+=i
    print(sum)

add()