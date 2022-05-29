def sqr(n):
    s=n*n
    return s
def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev    
n=int(input())
a=sqr(n)
b=reverse(n)
c=sqr(b)
if(a==reverse(c)):
    print('True')
else:
    print('False')
