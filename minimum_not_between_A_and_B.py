m=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
r=[]
for i in a:
    if i>=x and i<=y:
        f=1
    else:
        r.append(i)
if len(r)==0:
    print('-1')
else:
    print(min(r))