n=int(input())
s=0
k=n
while n:
    r=n%10
    n//=10
    fact=1
    for j in range(r,0,-1):
        fact*=j
    s+=fact
if s==k:
    print('The number',k,'is a strong number')
else:
    print('The number',k,'is not a strong number')