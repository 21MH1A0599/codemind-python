def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
c=0
d=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            c+=1
        else:
            d+=1
print(d)
