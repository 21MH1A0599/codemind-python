N=int(input())
for i in range(1,N+1):
    n=int(input())
    rev=0
    k=n
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    if rev==k:
        print('True')
    else:
        print('False')