def validate_roll_number():
    roll=input("Enter roll number : ")
    if roll[0:3]=="CSE" and roll[3:7]=="2026" and roll[7:]:
        print("Valid roll number")
    else:
        print("invalid roll number")

validate_roll_number()
    # CSE2026XXXX
    # 012345678910