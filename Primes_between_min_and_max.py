def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
mii=a.index(min(a))
mai=a.index(max(a))
c=0
if mii>mai:
    for i in range(mai,mii+1):
        if prime(a[i]):
            c+=1
else:
    for i in range(mii,mai+1):
        if prime(a[i]):
            c+=1
print(c)