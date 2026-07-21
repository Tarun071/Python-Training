def id_name():
    name=input().split()
    id_name=""
    for i in range(0,len(name)):
        id_name+=name[i][0].upper()
    print(id_name)
id_name()