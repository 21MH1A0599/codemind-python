a=input()
v=list('aeiou')
a=a.split()
for i in a:
    for j in i:
        if j in v:
            v.remove(j)
if len(v)==0:
    print(0)
else:
    print(*v)