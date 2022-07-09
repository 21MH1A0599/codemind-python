n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
f=0
r=[]
for i in a:
    if i>=x and i<=y:
        k=1
    else:
        r.append(i)
        f+=1
if len(r)==0:
    print('-1')
else:
    print(max(r))