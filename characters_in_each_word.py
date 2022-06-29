a=input()
a=a.split()
r=[]
for i in a:
    c=0
    for j in i:
        c+=1
    r.append(c)
print(*r)