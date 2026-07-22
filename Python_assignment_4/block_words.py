def block_words():
    blocked_list=["bastard","dog","donkey","stupid"]
    text=input().split()
    new_text=[]
    for i in range(0,len(text)):
            if text[i] in blocked_list:
                  new_text.append("*****")
            else:
                  new_text.append(text[i])
    print(" ".join(new_text))

block_words()