n=int(input())
for i in range(0,n):
    a=int(input())
    b=list(map(int,input().split()))
    for j in range(1,a+1):
        if j not in b:
            print(j)