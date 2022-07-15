a=input()
a=a.lower()
a=a.replace(" ","")
a=sorted(a)
r=[]
for i in a:
    if i not in r:
        r.append(i)
for i in r:
    if i!=' ':
        print(i,end='')