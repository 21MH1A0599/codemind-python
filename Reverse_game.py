def rev(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
n=int(input())
a=list(map(int,input().split()))
for i in a:
    c=rev(i)
    print(c,end=' ')