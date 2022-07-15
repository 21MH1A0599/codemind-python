n=input()
n=n.lower()
n=n.replace(" ","")
n=sorted(n)
r=[]
for i in n:
    if n.count(i)==1:
        r.append(i)
for i in r:
    if i!=' ':
        print(i,end='')