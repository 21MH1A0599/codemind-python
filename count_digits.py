n=int(input())
a=list(map(int,input().split()))
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
print(*r)