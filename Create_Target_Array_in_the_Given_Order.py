n=int(input())
a=list(map(int,input().split()))
n1=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(n):
    l.insert(b[i],a[i])
print(*l)