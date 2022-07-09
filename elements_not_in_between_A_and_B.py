n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
k,f=0,0
for i in a:
    if i>=x and i<=y:
        k=1
    else:
        print(i,end=' ')
        f+=1
if f==0:
    print('-1')