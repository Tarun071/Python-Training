def max_min_occuring_char():
    s=input()
    high=-111
    low=11111
    for i in s:
        if i!=" ":
            tot=s.count(i)
            if tot>high:
                high=tot
                high_char=i
            if tot<low:
                low=tot
                low_char=i
    print(f"MAximum occuring character : {high_char} {high}")
    print(f"Minimum occuring character : {low_char} {low}")
max_min_occuring_char()