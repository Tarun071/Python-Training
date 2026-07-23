def flatten(lst):
    for i in lst:
        if type(i) == list:
            yield from flatten(i)
        else:
            yield i

lst=eval(input())
ob=flatten(lst)
for i in ob:
    print(i,end=" ")