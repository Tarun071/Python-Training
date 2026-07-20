# def happy_number():
#     num=int(input("Enter number : "))
#     temp=num
#     while temp!=1 and temp!=4:
#         sum=0
#         while temp>0:
#             digit=temp%10
#             sum=sum+(digit**2)
#             temp=temp//10
#         temp=sum
#     if temp==1:
#         print("Happy Number")
#     else:
#         print("Not a Happy Number")
# happy_number()

n=194
while n!=1 and n!=4:
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem**2
        n//=10
    n=sum
    
if n==1:
    print("It is happy number")
else:
    print("It is not an happy number")
