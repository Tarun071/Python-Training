def classify_chars():
    s="hi this is a software trainee from miracle software solutions , Mcity @ bhogapuram, what are your question ?"
    words=0
    numbers=0
    vowels=0
    cons=0
    spcl=0
    for i in s:
        if i!=" ":
            if i.isnumeric():
                numbers+=1
            else:
                words+=1
                if i in "AEIOUaeiou":
                    vowels+=1
                elif i.isalpha():
                    cons+=1
                else:
                    spcl+=1
    print(f"words : {words} , numbers = {numbers} , vowels = {vowels} , cons = {cons} , spcl = {spcl}")
classify_chars()