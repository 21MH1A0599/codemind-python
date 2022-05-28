def rev(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
def sqr(n):
    s=n*n
    return s
n=int(input())
a=sqr(n)
b=rev(n)
c=sqr(b)
if a==rev(c):
    print('True')
else:
    print('False')