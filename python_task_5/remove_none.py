arr=[1,2,None,776,None,9]

res=list(map(lambda x:x is not None,arr))
print(res)