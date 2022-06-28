n=int(input())
rev=0
tem=n
while n:
    r=n%10
    rev=rev*10+r
    n//=10
if tem==rev:
    print('True')
else:
    print('False')