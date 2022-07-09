n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s,k=0,0                                                                                                                                                             
for i in a:
    if i>=x and i<=y:
        k=1
    else:
        s+=i
print(s)