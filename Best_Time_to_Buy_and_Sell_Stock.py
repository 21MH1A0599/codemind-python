n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i,n):
        if c<a[j]-a[i]:
            c=a[j]-a[i]
print(c)