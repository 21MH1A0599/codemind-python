n,k=map(int,input().split())
a=list(map(int,input().split()))
c,c1=0,0
for i in range(n):
    if a[i]<=k and c<=2:
        c1+=1
    if a[i]>k:
        c+=1
        if c==2:
            break
print(c1)