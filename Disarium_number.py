import math
n=int(input())
s=0
tem=n
l=int(math.log10(n))+1
while n:
    r=n%10
    s=s+r**l
    n//=10
    l-=1
if tem==s:
    print('True')
else:
    print('False')
    