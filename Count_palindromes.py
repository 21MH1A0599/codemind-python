def palin(n):
    rev=0
    t=n
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==t:
        return 1
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if palin(i):
        c+=1
print(c)