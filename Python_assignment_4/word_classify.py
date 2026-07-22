def word_classify():
    text=input()
    # text="hi hello good"
    total_chars=len(text)
    words=text.split()
    long=-111
    short=111
    sum=0
    for i in words:
        if len(i)>long:
            long=len(i)
        if len(i)<short:
            short=len(i)
        sum+=len(i)
    average=sum/len(words)

    print("Total characters :",total_chars)
    print("Total words : ",len(words))
    print("longest word :",long)
    print("Shortest word :",short)
    print("Average Word count :",average)
    print(sum)

word_classify()