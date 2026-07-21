def calculator():
    print("Arthematic calculator")
    print()
    num1,operator,num2=input("enter space after evrey input ").split()
    num1=int(num1)
    num2=int(num2)

    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        if num2==0:
            print("cannot divisible by zero")
        else:
            print(num1/num2)
    elif operator=="%":
        print(num1%num2)
while True:
    calculator()