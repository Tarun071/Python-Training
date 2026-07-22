def case_specify(text):
    upper_count=0
    lower_count=0
    for i in text:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    print(f"No. of uppercase characters : {upper_count}")
    print(f"No. of lowercase characters : {lower_count}")

s_input=input()
case_specify(s_input)