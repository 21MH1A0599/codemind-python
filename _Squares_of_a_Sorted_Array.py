n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    a[i]=a[i]**2
a.sort()
print(*a)

    