n=int(input())
a=list(map(int,input().split()))
k=int(input())
r=[]
for i in a:
    if k==a.count(i):
        if i not in r:
            r.append(i)
if len(r)==0:
    print('-1')
else:
    print(*r)