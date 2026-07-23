def answer(ar1,ar2):
    ans1=ar1+ar2
    ans2=ar1-ar2
    return ans1,ans2


ar1=[6, 5, 3, 9]
ar2=[0, 1, 7, 7]

result=list(map(answer,ar1,ar2))
print(result)