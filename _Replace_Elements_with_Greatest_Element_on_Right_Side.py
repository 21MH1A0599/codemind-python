n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    m=0
    for j in range(i+1,n):
        if m<a[j]:
            m=a[j]
    print(m,end=' ')
print("-1")