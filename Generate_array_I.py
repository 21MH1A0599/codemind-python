n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    if i%2==0:
        j=a[i]
        k=a[i+1]
        for i in range(0,k):
            l.append(j)
print(*l)