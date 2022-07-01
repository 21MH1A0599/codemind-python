n=int(input())
a=list(map(int,input().split()))
r=[]
c=0
for i in a:
    i=str(i)
    k=len(i)
    r.append(k)
for i in r:
    if i==max(r):
        c+=1
print(c)