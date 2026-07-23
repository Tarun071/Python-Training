def read_file(l):
    for i in l:
        yield i

txt=input().split()
ob=read_file(txt)
for i in ob:
    print(i)