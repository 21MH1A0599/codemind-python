def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
def square(n):
    c=n*n
    return c
n=int(input())
a=square(n)
b=reverse(n)
c=square(b)
if a==reverse(c):
    print('True')
else:
    print('False')