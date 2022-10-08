def balsum(a):
    t=sum(a)
    ad=0
    for i in a:
        if ad==t-i-ad:
            return "YES"
        ad+=i
    return "NO"
for i in range(int(input())):
    t=int(input())
    a=list(map(int,input().split()))
    print(balsum(a))