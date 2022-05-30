a=int(input())
for i in range(0,a):
    fact=1
    n=int(input())
    for i in range(1,n+1):
        fact*=i
    print(fact)