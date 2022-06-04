def pal(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    t=i
    if pal(i)==t:
        c+=1
print(c)