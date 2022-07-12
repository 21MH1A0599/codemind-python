n=int(input())
a=list(map(int,input().split()))
r=[]
r1=[]
for i in a:
    i=str(i)
    k=len(i)
    r.append(k)
for i in a:
    i=str(i)
    if len(i)==max(r):
        r1.append(i)
print(*r1)