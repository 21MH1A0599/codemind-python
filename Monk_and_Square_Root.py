for i in range(int(input())):
    a,b=map(int,input().split())
    c=max(a,b)
    f=0
    for i in range(c+1):
        if (i*i)%b==a:
            f=1
            break
    if f==0:
        print("-1")
    else:
        print(i)