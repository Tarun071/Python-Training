def listify(x):
    return list(x)

arr=input().split()
res=list(map(listify,arr))
print(res)
