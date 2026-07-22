def Pass_or_fail():
    marks=int(input())
    if marks<35:
        print("PASS")
        if marks>0 and marks>=35 and marks<60:
            print("Grade : C")
        elif marks>59 and marks<85:
            print("Grade : B")
        elif marks>84 and marks<101:
            print("Grade :A")
        else:
            print("Invalid marks")
    else:
        print("FAIL")
    
Pass_or_fail()