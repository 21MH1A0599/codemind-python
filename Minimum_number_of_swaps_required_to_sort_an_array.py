n=int(input())
a=list(map(int,input().split()))
x=a.copy()
x.sort()
c=0
for i in range(n):
    if a[i]!=x[i]:
        c+=1
        ind=a.index(x[i])
        a[i],a[ind]=a[ind],a[i]
print(c)