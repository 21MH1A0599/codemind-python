n=int(input())
a=list(map(int,input().split()))
r=[]
f=0
for i in a:
    if a.count(i)==i:
        if i not in r:
            f+=1
            r.append(i)
if f==0:
    print('-1')
else:
    print(min(r),max(r))