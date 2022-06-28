def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
def palin(n):
    rev=0
    tem=n
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==tem:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,100000):
    if prime(i):
        if palin(i):
            print(i)
            break
