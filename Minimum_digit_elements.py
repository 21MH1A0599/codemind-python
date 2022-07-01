n=int(input())
a=list(map(int,input().split()))
c=0
r=[]
for i in a:
    i=str(i)
    k=len(i)
    r.append(k)
for i in r:
    if i==min(r):
        c+=1
print(c)