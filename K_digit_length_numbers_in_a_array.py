x,y=map(int,input().split())
a=list(map(int,input().split()))
c=0
r=[]
for i in a:
    if i>=0:
        i=str(i)
        k=len(i)
        r.append(k)
    else:
        i=str(i)
        k=len(i)
        r.append(k-1)
for i in r:
    if i==y:
        c+=1
print(c)