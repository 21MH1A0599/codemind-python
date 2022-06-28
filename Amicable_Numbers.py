def fac(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
n=int(input())
m=int(input())
if fac(n)==m and fac(m)==n:
    print('Amicable')
else:
    print('Not Amicable')