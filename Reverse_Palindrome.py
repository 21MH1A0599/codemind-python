def rev(n):
    rev=0
    while n:
        rev=rev*10+n%10
        n//=10
    return rev
n=int(input())
while True:
    n=n+rev(n)
    if n==rev(n):
        break
print(n)