c=0
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(1,n):
        if a[j-1]>a[j]:
            c+=1
    if c==0:
        print(c)
    else:
        ma=max(a)
        mi=min(a)
        print(ma-mi)