n,d=map(int,input().split())
a=list(map(int,input().split()))
res=a[d:]+a[:d]
print(*res)