def square_elements(n):
    print(n*n)

arr=list(map(int,input().split()))
# arr=[2,3,4,5,6,6]
result=list(map(square_elements,arr))
print(result)