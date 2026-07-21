def skill_finder():
    resume_data=input().split()
    skills=['java', 'spring boot', 'sql','react']
    match=0
    checked=[]
    for i in resume_data:
        if i not in checked:
            checked.append(i)
            if i in skills:
                match+=1
    print(f"{match} skills are matching")

skill_finder()