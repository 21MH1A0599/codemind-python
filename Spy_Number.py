n=int(input())
s,m=0,1
tem=n
while n:
    r=n%10
    s+=r
    m*=r
    n//=10
if s==m:
    print('Spy Number')
else:
    print('Not Spy Number')