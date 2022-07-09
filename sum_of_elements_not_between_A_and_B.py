n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
r=[]
s=0
for i in a:
    if i>=x and i<=y:
        f=1
    else:
        s+=i
print(s)