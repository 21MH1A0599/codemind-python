n=int(input())
a=list(map(int,input().split()))
c=0
r=[]
for i in a:
    i=str(i)
    k=len(i)
    r.append(k)
l=max(r)
for i in r:
    if i==l:
        c+=1
print(c)
    